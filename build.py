import json



def main():
    input_file = open('bingo.json')
    txt = open('build/bingo.txt', "w")
    js  = open('build/bingo.js', "w")
    js.write('var bingoList = [];\n')

    data = json.load(input_file)
    input_file.close()
    
    list = []
    for i in range(0, 25):
        list.append([])
    
    for goal in data['goals']:
        for variant in goal['variants']:
            tier = variant[0]
            assert(tier >= 1 and tier <= 25)
            
            variant_text = goal['name'].replace('{X}', variant[1])
            if variant[1] == "1":
                variant_text = variant_text.replace("(s)", "")
                variant_text = variant_text.replace("(es)", "")
            else:
                variant_text = variant_text.replace("(s)", "s")
                variant_text = variant_text.replace("(es)", "es")
            
            goal['types']
            types = []
            for i in range(2, len(variant)):
                types.append(variant[i])
            types.extend(goal['types'])

            (list[tier-1]).append([types, variant_text])

            should_chaos = True
            for type_ in types:
                if type_.lower() == "finish-in":
                    should_chaos = False
                    break
            
            if should_chaos:
                txt.write("%s\n" % variant_text)

            del types
    txt.close()

    for tier in range(0, 25):
        js.write('bingoList[%d] = [\n' % (tier + 1))
        for goal in list[tier]:
            js.write('\t{\n\t\tname: \"%s\",\n' % goal[1])
            js.write('\t\ttypes: %s\n\t},\n' % str(goal[0]))
        js.write('];\n')
    js.close()

if __name__ == "__main__":
    main()
