from jinja2 import Template
import yaml
import os
import shutil
import sys

# Thanks :
# http://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte
# for resolving the encoding error
reload(sys)  
sys.setdefaultencoding('utf8')

languages = ["en","it","es","pt","fr"]

for language in languages:
    # Importing the language file
    yamlFile = language+".yaml"
    with open(yamlFile) as fYaml:
      languageYamlData =  yaml.load(fYaml)
    
    # Importing the template file
    templateFile = "index.j2"
    with open(templateFile) as fTemplate:
        template = Template(fTemplate.read())
        renderedPage = template.render(languageYamlData).encode( "utf-8" )
        
    # Create directory for the language
    languageDir = "../"+language
    if not os.path.exists(languageDir):
        os.makedirs(languageDir)
    os.chdir(languageDir)
        
    # Generate the file for the current language
    indexFile = "index.html"
    with open(indexFile, 'w') as config:
        config.write(renderedPage)
    os.chdir("../builder")
        

# Moving the English page to the root directory

src = "../en/index.html"
dst = "../index.html"
shutil.move(src, dst)
os.removedirs("../en");
