from pprint import pprint

import hashlib




message = [{"l":12,"s":"ly. The expe"},{"l":26,"s":"ibility of the first objec"},{"l":36,"s":"sing this data and knowing the lande"},{"l":35,"s":"compatible Objects;Value Rating;\n\nU"},{"l":24,"s":"ficient condition for in"},{"l":28,"s":"nd does not need to be incom"},{"l":33,"s":"pment in the following format: ID"},{"l":32,"s":"his task contains a list of equi"},{"l":19,"s":"e items of equipmen"},{"l":15,"s":"ost valuable eq"},{"l":34,"s":";Weight; Comma-Separated IDs of In"},{"l":7,"s":"'s land"},{"l":27,"s":"t with the second, the seco"},{"l":2,"s":"ne"},{"l":1,"s":"O"},{"l":23,"s":"o separate landers. Suf"},{"l":29,"s":"patible with the first, but t"},{"l":9,"s":"alfunctio"},{"l":38,"s":"ch), please write a program to select "},{"l":6,"s":"e ship"},{"l":10,"s":"ning. Two "},{"l":39,"s":"the most valuable equipment to load int"},{"l":30,"s":"hey cannot be loaded together "},{"l":13,"s":"dition team m"},{"l":20,"s":"t are incompatible t"},{"l":18,"s":"ers.\n\nHowever, som"},{"l":4,"s":" the"},{"l":22,"s":"and must be loaded int"},{"l":17,"s":"he operating land"},{"l":21,"s":"o be stored together "},{"l":41,"s":"the compatibility restrictions..........."},{"l":14,"s":"ust load the m"},{"l":37,"s":"rs maximum weight capacity (200 kg ea"},{"l":31,"s":"anyway.\n\nThe file attached to t"},{"l":11,"s":"operate ful"},{"l":16,"s":"uipment aboard t"},{"l":8,"s":"ers is m"},{"l":5,"s":" thre"},{"l":40,"s":"o the landers within the time limit and "},{"l":25,"s":"compatibility is incompat"},{"l":3,"s":" of"}]
# pprint(message)
pprint(
hashlib.md5(''.join([i['s'] for i in sorted(message, key=lambda s: s['l'])]).encode()).hexdigest()
)