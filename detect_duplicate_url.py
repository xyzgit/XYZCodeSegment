import fileinput, re
pattern = re.compile(r'\w+.do|\w+.json')
pattern_busid = re.compile(r'(busid:){1}(.*\')(.*)(\')')
list = [];
for line in fileinput.input(files=('/Users/xyz/workspace/code_source/sencha/webapp/app/loanfoundation/LoanRequest.js')):
        match = pattern.search(line);
        if match:
            name = match.group();
            if  name in list:
                    print 'duplicate:' + name
                    continue
            if name != 'queryPersonalLoan.do':
                    list.append(name)

        match = pattern_busid.search(line.strip());
        if match:
            name = match.group(3);
            if  name in list:
                    print 'duplicate:' + name
                    continue
            list.append(name)

for request in list:
        print request
print 'total request number: {0}'.format(len(list))
