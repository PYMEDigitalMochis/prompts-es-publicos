#!/usr/bin/env python3
"""Pruebas deterministas de contenido: no ejecutan los prompts en un LLM."""
import json,re,unittest
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
ITEMS=json.loads((BASE/'tests'/'casos.json').read_text(encoding='utf-8'))
FILES=sorted((BASE/'prompts').rglob('*.md'))
class BibliotecaTests(unittest.TestCase):
 def test_01_thirty_cases(self): self.assertEqual(len(ITEMS),30)
 def test_02_thirty_prompts(self): self.assertEqual(len(FILES),30)
 def test_03_unique_ids(self): self.assertEqual(len({x['id'] for x in ITEMS}),30)
 def test_04_all_cases_resolve(self):
  for x in ITEMS:
   with self.subTest(id=x['id']): self.assertTrue((BASE/x['file']).is_file())
 def test_05_structure_and_placeholders(self):
  for x in ITEMS:
   with self.subTest(id=x['id']):
    c=(BASE/x['file']).read_text(encoding='utf-8')
    self.assertIn('id: '+x['id']+'\n',c)
    self.assertIn('version: 1.1.0',c)
    self.assertIn('estado: probado-manualmente-no',c)
    for section in ('## Prompt listo para copiar','## Comprobación del resultado','**Campos a personalizar:**'): self.assertIn(section,c)
    decl=re.search(r'\*\*Campos a personalizar:\*\* (.+)',c).group(1)
    self.assertEqual(set(re.findall(r'\[([A-Z0-9_]+)\]',decl)),set(x['variables']))
    body=c.split('## Prompt listo para copiar',1)[1].split('## Comprobación del resultado',1)[0]
    for k,v in x['variables'].items():
     self.assertIn('['+k+']',body)
     self.assertTrue(v.strip())
    # Variables usadas en el texto del prompt deben figurar en el inventario.
    self.assertEqual(set(re.findall(r'\[([A-Z][A-Z0-9_]+)\]',body)),set(x['variables']))
 def test_06_catalog_links(self):
  catalog=(BASE/'CATALOGO.md').read_text(encoding='utf-8')
  links=re.findall(r'\]\((prompts/[^)]+\.md)\)',catalog)
  self.assertEqual(len(links),30)
  self.assertEqual(set(links),{x['file'] for x in ITEMS})
  for link in links:self.assertTrue((BASE/link).is_file())
 def test_07_document_links(self):
  for fname in ['README.md','GUIA_DE_USO.md']:
   c=(BASE/fname).read_text(encoding='utf-8')
   for link in re.findall(r'\]\((?!https?://)([^)#]+\.md)\)',c):
    with self.subTest(file=fname,link=link):self.assertTrue((BASE/link).is_file())
 def test_08_security_screen(self):
  forbidden=[r'(?i)pymedigital@proton\.me',r'(?i)app\.notion\.com/p/',r'(?i)dropbox\.com/',
             r'(?i)PYME[\s_-]+Digital',r'(?i)GrokPyME',r'(?i)Ámbar del Norte',r'(?i)Detrás del Botón',
             r'gh[pousr]_[a-zA-Z0-9_]{20,}',r'github_pat_[a-zA-Z0-9_]{20,}',r'AKIA[A-Z0-9]{16}',
             r'-----BEGIN [A-Z ]*PRIVATE KEY-----',r'(?i)\bsk-[A-Za-z0-9_-]{20,}']
  for p in BASE.rglob('*'):
   if p.suffix not in {'.md','.json','.yml','.py'}:continue
   if p.name=='validar_biblioteca.py':continue # regex names of secrets are test fixtures
   data=p.read_text(encoding='utf-8')
   for pattern in forbidden:
    with self.subTest(path=str(p),pattern=pattern):self.assertIsNone(re.search(pattern,data))
 def test_09_license(self):
  lic=(BASE/'LICENSE.md').read_text(encoding='utf-8')
  self.assertIn('CC-BY-4.0',lic)
  self.assertIn('creativecommons.org/licenses/by/4.0/legalcode',lic)
 def test_10_five_scenarios_documented(self):
  c=(BASE/'PRUEBAS_Y_LIMITACIONES.md').read_text(encoding='utf-8')
  for id in ('INV-001','PROY-001','DEV-001','NEG-002','APR-001'):self.assertIn(id,c)
 def test_11_github_action(self): self.assertTrue((BASE/'.github/workflows/validar.yml').is_file())
if __name__=='__main__':unittest.main(verbosity=2)
