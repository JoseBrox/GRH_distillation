#!/usr/bin/env python3
"""Authenticate the quadratic-host obstruction and exact elementary identities.

This does not prove the unresolved determinant comparison, replay a Lean
kernel, or claim that every admissible host descends to a quadratic field.
"""
from fractions import Fraction as F
from math import isqrt
import gzip
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/quadratic-host-descent-obstruction.md"
OUT = "certificates/quadratic-host-descent-obstruction.json"
SOURCES = [
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification.TwoWeightEqOneAddRoot",
     "3646386e9cd25287a50eb1ad82456c5b26316207741b8ed7298d46aa4f9d7826", [[14,26]]),
    ("Development.AutomorphicSpectrum.Definitions.GlobalGeometry.IsHodgeLine",
     "5527f8f1c2fd9a12831afa19dc9e009ca7f5e211f7f61075d3a86228eea1d9ef", [[15,23]]),
    ("Development.WeilBound.CoreStatements.PlurisubharmonicCones.FlatSat",
     "f34edb87ca7a8196a91080cf3435510c6c33e6fc1de14c9d976d82db95f423d8", [[11,20]]),
]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def record_file(path):
    data = (ROOT/path).read_bytes()
    return {"path":path,"bytes":len(data),"sha256":sha(data)}

def sources():
    packed = (ROOT/'blueprint/lean-source-imports.json.gz').read_bytes()
    inventory = json.loads((ROOT/'certificates/lean-source-inventory.json').read_text())
    assert sha(packed) == inventory['compressed_graph']['sha256']
    atlas = json.loads(gzip.decompress(packed))
    assert atlas['commit'] == REV and atlas['repository'] == 'jsmorph/rh'
    blobs = {r[0]:r[1] for r in atlas['modules']}
    results=[]
    for module,expected,ranges in SOURCES:
        rel='lean/src/'+module.replace('.','/')+'.lean'
        candidates=[ROOT/'build/source-cache/jsmorph/rh'/REV/rel,ROOT/'build/lean-mirror'/rel]
        local=next((p for p in candidates if p.is_file()),None)
        if local is None: raise FileNotFoundError('Populate source_excerpt.py cache: '+module)
        data=local.read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert sha(data)==expected and blob==blobs[module]
        lines=data.splitlines()
        ex=[]
        for start,end in ranges:
            assert 1<=start<=end<=len(lines) and end-start<120
            ex.append({'lines':[start,end],'sha256':sha(b'\n'.join(lines[start-1:end])+b'\n')})
        results.append({'module':module,'path':rel,'sha256':expected,'git_blob_sha1':blob,
                        'line_count':len(lines),'inspected_excerpts':ex})
    return results

def exact_checks():
    import sympy as sp
    w,d,X,Y,T,delta,nu=sp.symbols('w d X Y T delta nu')
    f=w*w-w+(d+1)/4
    assert sp.expand(4*f-((2*w-1)**2+d))==0
    assert sp.expand(sp.discriminant(f,w)+d)==0
    assert sp.diff(f,w)==2*w-1
    degree=X+Y+delta
    assert sp.expand(degree-(2*T-(X-Y)+delta+2*(X-T)))==0
    primes=[]
    for p in range(7,2001,16):
        if all(p%q for q in range(2,isqrt(p)+1)):
            t=pow(2,-1,p)
            c=(p+1)//4
            assert (t*t-t+c)%p==0 and (2*t-1)%p==0
            assert (1-4*c)==-p
            primes.append(p)
    finite=0
    for x,y,delta,nu in itertools.product([F(-3),F(0),F(5)], [F(-2),F(0),F(4)],
                                         [F(0),F(1,3),F(7)], [F(0),F(1,2),F(6)]):
        t=x-nu
        deg=x+y+delta
        assert deg==2*t-(x-y)+delta+2*nu
        finite+=1
    return {'symbolic_polynomial_discriminant_derivative_and_index_identities':'PASS',
            'residue_field_prime_cases':len(primes),'exact_signed_index_cases':finite,
            'scope':'The written proof establishes ramification for every allowed prime; finite examples are consistency checks only.'}

def main():
    src=sources()
    checks=exact_checks()
    result={'schema_version':1,'result':'PASS',
            'claim':'The proposed imaginary-quadratic host violates the actual unramifiedness hypothesis; determinant grouping alone supplies no degree comparison.',
            'source_revision':{'repository':'jsmorph/rh','commit':REV},
            'sources':src,'checks':checks,'independent_reviews':[
                {'reviewer':'/root','result':'PASS',
                 'scope':'Full ordinary-mathematics review: integral-basis denominator argument, discriminant, prime ideal and differential ramification proof; positive index signs and grouping identity; explicit limited scope. Independently hash-read all three recorded source excerpts through source_excerpt.py; no upstream proof replay.'},
                {'reviewer':'/root/rh_source_symmetry','result':'PASS',
                 'scope':'Independent ordinary-mathematics review of all three sections and independent hash verification and reading of all three recorded source excerpts. Confirms that unramifiedness is an actual Host hypothesis, coefficient-field extension does not repair it, and determinant grouping supplies no signed degree bound. No upstream geometric proof or Lean-kernel replay audited.'}],
            'limitations':['No determinant/period or point-height inequality is proved.',
                           'No source-compatible quadratic-host application is claimed.',
                           'No upstream geometric proof or Lean-kernel replay is performed.'],
            'artifacts':[record_file(NOTE),record_file('scripts/check_quadratic_host_descent_obstruction.py')]}
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:',len(src),'pinned files; 3 bounded excerpts;',checks['residue_field_prime_cases'],
          'prime residue checks;',checks['exact_signed_index_cases'],'signed index cases.')

if __name__=='__main__': main()
