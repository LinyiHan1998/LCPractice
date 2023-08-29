def request_parser(valid_auth_tokens, requests):
    result = []
    valid_auth_tokens_set = set(valid_auth_tokens)
    for i in range(len(requests)):
        pos = requests[i][1].index('?') + 1
        parameters = requests[i][1][pos:].split('&')
        parameters_dict = {item.split('=')[0]: item.split('=')[1] for item in parameters}
        print(parameters_dict)

        if ("token" not in parameters_dict or
            parameters_dict["token"] not in valid_auth_tokens_set):
            result.append("INVALID")
            continue

        parameters_dict.pop("token", None)
        if (requests[i][0] == 'GET' or
                (requests[i][0] == 'POST' and
                 "csrf" in parameters_dict and
                 bool(re.fullmatch(r'[a-z0-9]+', parameters_dict["csrf"])) and
                 len(parameters_dict["csrf"]) >= 8)):

            parameters_dict.pop("csrf", None)
            tmp = ','.join([str(k) + ',' + str(v) for k, v in parameters_dict.items()])
            result.append("VALID," + tmp)
        else:
            result.append("INVALID")

    return result