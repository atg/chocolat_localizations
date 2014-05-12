import os
from os.path import join as jp
from subprocess import check_call, check_output

assert os.path.basename(os.getcwd()) == 'chocolat'

# Generate strings for nibs
for xib in os.listdir('ui'):
    name, ext = os.path.splitext(xib)
    if not ext == '.xib':
        continue
    
    if name.lower().endswith('backup'): continue
    if name.endswith('_'): continue
    if name.startswith('CHProjectFind'): continue
    if name.startswith('CHPreferenceWindow'): continue
    if name.startswith('CHQuickOpen'): continue
    if name.startswith('CHSyntaxInspector'): continue
    if name.startswith('CHWebPreview'): continue
    if name.startswith('CHLaunchBar'): continue
    print xib
    # ibtool --generate-strings-file locale/chocolat_localizations/en-us/MainMenu.strings ui/MainMenu.xib
    check_call([
        '/usr/bin/ibtool',
        '--generate-strings-file',
        jp('locale/chocolat_localizations/en-us', name + '.strings'),
        jp('ui', xib),
    ])

