import sys
sys.path.append('./User')
from User import User

args = sys.argv
so_url = args[1]
regions = args[2:]

try:
    so_user = User(so_url)
    so_user.build_profile_info(regions)
    print(so_user.user_name + " has a reputation of " + "{0:,}".format(so_user.reputation))
    if so_user.relative_ranking:
        print(so_user.user_name + "'s relative ranking:")
        for region in so_user.relative_ranking:
            print("\tTop " + str(so_user.relative_ranking[region]) + "% in the region " + region)

except Exception as e:
    print(str(e))