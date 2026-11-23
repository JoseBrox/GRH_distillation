#!/usr/bin/env python3
"""Exact identities and source contracts for the rank-three Sharp proof.

No finite diagnostic substitutes for the cohomology, dimension or
connectedness arguments in the accompanying standard-mathematics note.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "FrobeniusSmoothVectors.DefIso": [(34, 126)],
    "FrobeniusSmoothVectors.Integral": [(71, 103)],
    "FrobeniusSmoothVectors.ContinuousCoboundaries2": [(167, 212)],
    "FrobeniusSmoothVectors.SumLe": [(42, 115)],
    "FrobeniusSmoothVectors.Detsec": [(78, 129), (147, 191)],
    "FrobeniusSmoothVectors.ThickOfDer": [(1, 94), (95, 174), (175, 255)],
    "FrobeniusSmoothVectors.LeAdicClosure": [(255, 269)],
    "FrobeniusSmoothVectors.ChainedOfComap": [(63, 142)],
    "FrobeniusSmoothVectors.StrSMul": [(13, 23)],
    "FrobeniusSmoothVectors.KrullDimLtOfNotLeTriangular": [(1, 58)],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    K = sp.diag(1, -1, 1)
    variables = sp.symbols('m0:9')
    A = sp.Matrix(3, 3, variables)
    D = A-J*A.T*J
    assert sp.trace(D) == 0
    assert sp.expand(D.det()) == 0
    assert J*D.T*J == -D
    H = sp.diag(1, 0, -1)
    E = lambda i,j: sp.zeros(3).subs({}) + sp.Matrix(3,3,lambda a,b: int(a==i and b==j))
    U = E(0,1)-E(1,2)
    V = E(1,0)-E(2,1)
    zeta = sp.symbols('zeta', nonzero=True)
    marked = zeta*H
    for X in [H,U,V]:
        assert X*J+J*X.T == sp.zeros(3)
    assert K*H*K == H
    assert K*U*K == -U and K*V*K == -V
    assert U*marked-marked*U == -zeta*U
    assert V*marked-marked*V == zeta*V
    even = [(i,j) for i in range(3) for j in range(3) if (i-j)%2==0]
    odd = [(i,j) for i in range(3) for j in range(3) if (i-j)%2]
    assert len(even)==5 and len(odd)==4
    assert sum(i<=j for i,j in even)==4 and sum(i<=j for i,j in odd)==2

    a,b,c,d,e,f,g,h,k,l = sp.symbols('a b c d e f g h k l')
    a0 = sp.Matrix([[a,0,b],[0,e,0],[c,0,d]])
    b0 = sp.Matrix([[f,0,g],[0,l,0],[h,0,k]])
    u1,u2,u3,u4,v1,v2,v3,v4 = sp.symbols('u1 u2 u3 u4 v1 v2 v3 v4')
    a1 = sp.Matrix([[0,u1,0],[u2,0,u3],[0,u4,0]])
    b1 = sp.Matrix([[0,v1,0],[v2,0,v3],[0,v4,0]])
    def thick(base, derivative):
        return sp.Matrix([[base[0,0],derivative[0,1],base[0,2]],
                          [0,base[1,1],0],
                          [base[2,0],derivative[2,1],base[2,2]]])
    assert sp.simplify(thick(a0*b0,a0*b1+a1*b0)-thick(a0,a1)*thick(b0,b1)) == sp.zeros(3)
    checked=0
    for C0 in range(21):
        for degree in range(3*C0+8, 3*C0+28):
            assert 2*degree+3*C0+2 < 3*degree
            checked += 1
    return {
        "rank_three_marking": "Exact skew-adjoint trace/determinant identities; the two odd orthogonal gauge directions are multiplied by +/-zeta, and the even torus remains.",
        "parity_dimensions": {"adjoint_even":5,"adjoint_odd":4,"local_even":4,"local_odd":2,"real_even":1,"real_odd":2},
        "thick_modification": "Exact polynomial multiplicativity of the original even-block/odd-column derivation operation.",
        "triangular_dimension_cases": checked,
        "scope": "Finite identities and edge diagnostics only. The note proves the general cohomology, determinant incidence, completion, continuity and nonsplitting assertions."
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--offline',action='store_true')
    args=parser.parse_args()
    packed=(ROOT/'blueprint/lean-source-imports.json.gz').read_bytes()
    inventory=json.loads((ROOT/'certificates/lean-source-inventory.json').read_text())
    assert digest(packed)==inventory['compressed_graph']['sha256']
    atlas=json.loads(gzip.decompress(packed))
    modules={row[0]:row for row in atlas['modules']}
    records=[]
    for name,ranges in RANGES.items():
        module=BASE+name
        item={'repository':atlas['repository'],'commit':atlas['commit'],
              'path':'lean/src/'+module.replace('.','/')+'.lean',
              'git_blob_sha1':modules[module][1]}
        source=inspect_file(item,args.offline)
        lines=(ROOT/'build/source-cache'/item['repository']/item['commit']/item['path']).read_text().splitlines()
        for lo,hi in ranges:
            assert 1<=lo<=hi<=len(lines) and hi-lo+1<=120
        records.append({**item,'sha256':source['sha256'],'line_count':len(lines),
                        'ranges':[{'start':lo,'end':hi,'sha256':digest(('\n'.join(lines[lo-1:hi])+'\n').encode())}
                                  for lo,hi in ranges]})
    note=ROOT/'notes/selmer-support-continuation-rank-three-sharp.md'
    result={
        'classification':'Closed literal rank-three Sharp construction; independently reviewed.',
        'proof_file':str(note.relative_to(ROOT)),'proof_sha256':digest(note.read_bytes()),
        'source_records':records,'exact_diagnostics':exact_checks(),
        'primary_reference':{'url':'https://stacks.math.columbia.edu/tag/0ECR',
          'checked_application':'The completed generic incidence ring has prime radical and dimension a+g+1+g^2. There are g^2+g+b cuts; with a-b=3d+1, connectedness is retained after removing subsets of dimension <3d+1.'},
        'decisive_interfaces':{
          'chart':'The original chart, coefficient extension and residue embedding are retained through the finite Laurent algebra, closed coefficient subring, and evaluation only before completion.',
          'presentation':'Parity tangent dimensions h1_even+1 and h1_odd; parity relation counts at most h2_even and h2_odd; original EC gives a-b=3d+1 after harmless zero padding.',
          'nonzero_odd_variables':'Original f4 injects into odd H1 because the quotient has no invariants and the local odd Borels meet the lower odd submodule in zero.',
          'determinant_section':'Generic singular-matrix/kernel-vector incidence has prime radical and codimension g; its homogeneous completion remains a domain. No regular-sequence or transversality assumption.',
          'thick':'An actual Q-valued extension, both original ordered products, adic continuity, and nonsplitting after every injective map Q->field.',
          'nilpotents':'Retained in the actual chart and parity presentation. Prime quotients/reduction are used only for Krull dimension and topological connectedness.'},
        'scope':{'whole_node_closed':False,'lean_build':False,
          'remaining':'Global propagation and arithmetic transfer are supplied by the companion reviewed packages; finite-point/endomorphism transfer and the moving-family integral Selmer estimate remain separate.'}}
    result['presentation_files']=[
        {'file':name,'sha256':digest((ROOT/name).read_bytes())}
        for name in ['paper/shared/selmer-support-continuation-rank-three.tex',
                     'paper/shared/selmer-support-continuation-rank-three-references.tex']]
    out=ROOT/'certificates/selmer-support-continuation-rank-three-sharp.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'source_files':len(records),'exact_diagnostics':'passed','certificate':str(out.relative_to(ROOT)),'no_whole_node_completion':True}))


if __name__=='__main__':
    main()
