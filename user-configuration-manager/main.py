def add_setting(configDict,keyValueSet):
    keyValueSetLower = tuple((item.lower()if isinstance(item,str)  else item) for item in keyValueSet)
    if keyValueSetLower[0] in configDict:
        return f'Setting \'{keyValueSetLower[0]}\' already exists! Cannot add a new setting with this name.'
    else:
        configDict[keyValueSetLower[0]] = keyValueSetLower[1]
        return f'Setting \'{keyValueSetLower[0]}\' added with value \'{keyValueSetLower[1]}\' successfully!'
def update_setting(configDict,keyValueSet):
    keyValueSetLower = tuple((item.lower()if isinstance(item,str)  else item) for item in keyValueSet)
    if keyValueSetLower[0] in configDict:
        configDict[keyValueSetLower[0]] = keyValueSetLower[1]
        return f'Setting \'{keyValueSetLower[0]}\' updated to \'{keyValueSetLower[1]}\' successfully!'
    else:
        return f'Setting \'{keyValueSetLower[0]}\' does not exist! Cannot update a non-existing setting.'
def delete_setting(configDict,key):
    keylower = key.lower()
    if keylower in configDict:
        del configDict[keylower]
        return f'Setting \'{keylower}\' deleted successfully!'
    else:
        return f'Setting not found!'
def view_settings(configDict):
    if len(configDict) < 1:
        return 'No settings available.'
    messageReturn = 'Current User Settings:\n'
    for key,value in configDict.items():
        messageReturn += f'{key.capitalize()}: {value}\n'
    return messageReturn
test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}    
print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(view_settings(test_settings))