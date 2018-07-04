## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file main.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_311 = Integer(311); _sage_const_375 = Integer(375); _sage_const_0 = Integer(0); _sage_const_306 = Integer(306); _sage_const_1 = Integer(1)## This file (main.sagetex.sage) was *autogenerated* from main.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('main', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_306 
_st_.blockbegin()
try:
 #Consideremos el grafo de Errera
 Q = graphs.ErreraGraph()
 ErrPolyCrom = Q.chromatic_polynomial()
 ErrNumCrom = Q.chromatic_number()
except:
 _st_.goboom(_sage_const_311 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_375 
 _st_.inline(_sage_const_0 , latex(ErrNumCrom))
except:
 _st_.goboom(_sage_const_375 )
try:
 _st_.current_tex_line = _sage_const_375 
 _st_.inline(_sage_const_1 , latex(ErrPolyCrom))
except:
 _st_.goboom(_sage_const_375 )
_st_.endofdoc()
