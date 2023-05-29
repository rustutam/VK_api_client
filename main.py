from vk_app import VK_App
import argparse
import re


def print_friends(string):
    pattern = r">(\w+)\s(\w+)<"
    friends = re.findall(pattern, string)
    print(friends)
    len_s = 25
    print("-" * len_s)
    for human in friends:
        first_name = human[1]
        last_name = human[0]
        print(f"First Name: {first_name}\n"
              f"Last Name: {last_name}")
        print("-" * len_s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-uid", required=True)
    parser.add_argument("-aid", required=True, help="id of vk application")
    parser.add_argument("-tkn", required=True,
                        help="access_token of vk_app")
    cnsl_args = parser.parse_args().__dict__
    protocols_app = VK_App(cnsl_args["aid"], cnsl_args["tkn"])
    user_id = cnsl_args["uid"]
    rep = protocols_app.get_friends_list(user_id)['items']
    res = "\n".join(["<p>" + f'<a href="https://vk.com/id{repl["id"]}">'
                     + repl['last_name'] + " " + repl['first_name']
                     + "</a>" + "</p>" for repl in rep])
    print_friends(res)
