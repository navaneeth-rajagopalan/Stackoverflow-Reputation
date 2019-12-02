import sys
sys.path.append('./User')
from User import User

#try:
me = User('https://stackoverflow.com/users/4833507/Navaneeth')
me.build_profile_info(['Melbourne', 'Sydney', 'Bengaluru'])
print(me.user_name + " has a reputation of " + "{0:,}".format(me.reputation))
if me.relative_ranking:
    print(me.user_name + "'s relative ranking:")
    for region in me.relative_ranking:
        print("\ttop " + str(me.relative_ranking[region]) + "% in the region " + region)

dkularni = User('https://stackoverflow.com/users/696257/dkulkarni')
dkularni.build_profile_info(['Melbourne', 'Sydney', 'Bengaluru'])
print(dkularni.user_name + " has a reputation of " + "{0:,}".format(dkularni.reputation))
if dkularni.relative_ranking:
    print(dkularni.user_name + "'s relative ranking:")
    for region in dkularni.relative_ranking:
        print("\ttop " + str(dkularni.relative_ranking[region]) + "% in the region " + region)
# except Exception as e:
#     print(str(e))