import os



files_ip_path = "/home/flask/services/script/data/DEV_SW/"

def create_ip_dict_fromfile(files_ip_path) -> dict:
    ip_dict = dict()
    # print(st)
    i = next(os.walk(files_ip_path))
    for j in i[2]:
        if j[:3] == 'SW_' and j[-4:] == '.txt':
            with open(f'{i[0]}{j}', 'r', encoding='UTF-8') as ip_list:
                for ip in ip_list.read().strip().split():
                    n = j[3:-4]
                    if n in ip_dict:
                        ip_dict[n].add(ip)
                    else:
                        ip_dict[n] = {ip}

    return ip_dict



if __name__ == '__main__':
    print(create_ip_dict_fromfile(files_ip_path))
