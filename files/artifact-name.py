import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("spec_file")
args = parser.parse_args()

spec_file = args.spec_file

with open(spec_file) as fh:
    lines = fh.readlines()

# Possible values to search for
# Name: %{name_name}
# Name: name_name
for line in lines:
    if re.search("Name.*:", line):
        name = line.split(":")[1].strip()
        break
else:
    print("Did not find name in spec file")
    exit(1)

# If name value is a macro
# e.g.
# %global name_name projectname
# Name: %{name_name}
if re.search("%\{.+\}", name):
    name_ = name.replace("%", "").replace("{", "").replace("}", "")
    for line in lines:
        if "%global" in line and name_ in line:
            line_ = re.sub(" {2,}", " ", line.strip())
            name = line.split()[-1]
            break

print(name)
