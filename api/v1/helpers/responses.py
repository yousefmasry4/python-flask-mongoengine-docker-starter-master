def remove_oid(string):
    def rmOid(obj: dict):
        id = obj['_id']['$oid']
        obj.pop('_id')
        obj['id'] = id
        return obj

    if type(string) == list:
        for i in range(len(string)):
            rmOid(string[i])
    else:
        rmOid(string)
    return string
