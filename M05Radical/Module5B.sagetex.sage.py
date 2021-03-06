## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file /media/archdoc/7636-BC29/improvedExamGeneration/M05Radical/Module5B.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_115 = Integer(115); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_135 = Integer(135); _sage_const_65 = Integer(65); _sage_const_44 = Integer(44); _sage_const_89 = Integer(89); _sage_const_49 = Integer(49); _sage_const_86 = Integer(86); _sage_const_138 = Integer(138); _sage_const_68 = Integer(68); _sage_const_155 = Integer(155); _sage_const_13 = Integer(13); _sage_const_38 = Integer(38); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_62 = Integer(62); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_118 = Integer(118); _sage_const_121 = Integer(121); _sage_const_12 = Integer(12); _sage_const_92 = Integer(92); _sage_const_141 = Integer(141)## This file (Module5B.sagetex.sage) was *autogenerated* from Module5B.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('Module5B', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_35 
_st_.blockbegin()
try:
 load("../Code/generalPurposeMethods.sage")
 load("../Code/keyGeneration.sage")
except:
 _st_.goboom(_sage_const_38 )
_st_.blockend()
_st_.current_tex_line = _sage_const_44 
_st_.blockbegin()
try:
 moduleNumber = _sage_const_5 
 version = "B"
 problemNumber = _sage_const_21 
 load("../Code/radical/domainRadical.sage")
except:
 _st_.goboom(_sage_const_49 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_0 , latex(displayStem))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_1 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_2 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_3 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_4 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_5 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_6 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_62 )
_st_.current_tex_line = _sage_const_65 
_st_.blockbegin()
try:
 problemNumber = _sage_const_22 
 load("../Code/radical/radicalGraphToEquation.sage")
except:
 _st_.goboom(_sage_const_68 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_7 , latex(displayStem))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_8 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_9 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_10 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_11 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_86 )
_st_.current_tex_line = _sage_const_89 
_st_.blockbegin()
try:
 problemNumber = _sage_const_23 
 load("../Code/radical/radicalEquationToGraph.sage")
except:
 _st_.goboom(_sage_const_92 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_115 
 _st_.inline(_sage_const_12 , latex(displayStem))
except:
 _st_.goboom(_sage_const_115 )
try:
 _st_.current_tex_line = _sage_const_115 
 _st_.inline(_sage_const_13 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_115 )
_st_.current_tex_line = _sage_const_118 
_st_.blockbegin()
try:
 problemNumber = _sage_const_24 
 load("../Code/radical/solveRadicalLinear.sage")
except:
 _st_.goboom(_sage_const_121 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_14 , latex(displayStem))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_15 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_16 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_17 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_18 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_19 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_20 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_135 )
_st_.current_tex_line = _sage_const_138 
_st_.blockbegin()
try:
 problemNumber = _sage_const_25 
 load("../Code/radical/solveRadicalQuadratic.sage")
except:
 _st_.goboom(_sage_const_141 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_21 , latex(displayStem))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_22 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_23 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_24 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_25 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_26 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_27 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_155 )
_st_.endofdoc()

