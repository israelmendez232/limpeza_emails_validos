# Script para Validar Email Marketing em PY

Script para classificar os emails de um csv se são válidos ou não, fazendo uma limpeza mais profunda. Ele contém os seguintes filtros (em ordem, para não consumir tanto processamento):
- REGEX;
- DNS. Como instalar: https://stackoverflow.com/questions/21641696/python-dns-module-import-error ou código abaixo:

```python
git clone https://github.com/rthalley/dnspython
cd dnspython/
python setup.py install
```
- SMTP.
