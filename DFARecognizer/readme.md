# Reconhecedor de autômatos finitos determinísticos

Implementação de um código capa de reconhecer expressões regulares/cadeias de autômatos finitos determinísticos (AFD's).

Além disso, também é implementada uma classe auxiliar que serve como um "leitor de expressão",
cujo objetivo é receber uma expressão regular (*e.g. 010, 0\*1, 0\+1*) e transfromar em um modelo
o qual o arquivo *dfa.py* reconheça, a saber, um dicionário que segue o padrão:

+ {
    "Estado\_i" : {"Simbolo\_aceito":"Próximo\_Estado"},
    	 .		    .		      .        ,
    	 .                  .                 .        ,
	 .		    .                 .        ,
    "Estado\_n" : {"Simbolo\_aceito":       "-1"      }
   }

### Autores
+  Vitor Acosta da Rosa
+  Rubens de Araújo Rodrigues Mendes
+  Rafael Zacarias Palierini
+  Andy Silva Barbosa
