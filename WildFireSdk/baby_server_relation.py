from baby_server import BabyServer


# https://docs.wildfirechat.cn/server/admin_api/user_relation.html
# obaby@mars
# by:obaby
# http://www.h4ck.org.cn
# http://www.obaby.org.cn
# http://www.findu.co

class BabyRelations(BabyServer):

    def set_friendship(self, user_id, friend_uid, status):
        '''
        http://domain:18080/admin/friend/status
        参数	类型	必需	描述
        userId	string	是	用户ID
        friendUid	string	是	对方ID
        status	int	是	双方关系，0为好友，1为陌生人
        好友关系与黑名单关系是分开的，如果处理黑名单请用黑名单接口
        :param user_id:
        :param friend_uid:
        :param status:
        :return:
        '''
        data = {'userId': user_id,
                'friendUid': friend_uid,
                'status': str(status)}

        url = self.format_request_url('/admin/friend/status')
        return self.baby_post(url, data)

    def get_friend_list(self, user_id):
        '''
        http://domain:18080/admin/friend/list
        参数	类型	必需	描述
        userId	string	是	用户ID
        :return:
        '''
        data = {'userId': user_id}
        url = self.format_request_url('/admin/friend/list')
        return self.baby_post(url, data)

    def set_black_list(self, user_id, friend_uid, status):
        '''
        http://domain:18080/admin/blacklist/status
        参数	类型	必需	描述
        userId	string	是	用户ID
        targetUid	string	是	对方ID
        status	int	是	双方关系，0为取消黑名单，1为设置为黑名单
        :return:
        '''
        data = {'userId': user_id,
                'friendUid': friend_uid,
                'status': str(status)}

        url = self.format_request_url('/admin/blacklist/status')
        return self.baby_post(url, data)

    def get_blacklist_list(self, user_id):
        '''
        http://domain:18080/admin/blacklist/list
        参数	类型	必需	描述
        userId	string	是	用户ID
        :param user_id:
        :return:
        '''
        data = {'userId': user_id}
        url = self.format_request_url('/admin/blacklist/list')
        return self.baby_post(url, data)

    def set_alias(self, operator, target_id, alias):
        '''
        http://domain:18080/admin/friend/set_alias
        参数	类型	必需	描述
        operator	string	是	用户ID
        targetId	string	是	对方ID
        alias	string	否	备注名
        :param user_id:
        :return:
        '''
        data = {'operator': operator,
                'targetId': target_id,
                'alias': str(alias)}

        url = self.format_request_url('/admin/friend/set_alias')
        return self.baby_post(url, data)

    def get_alias(self, operator, target_id):
        '''
        http://domain:18080/admin/friend/get_alias
        参数	类型	必需	描述
        operator	string	是	用户ID
        targetId	string	是	用户ID
        :param operator:
        :param target_id:
        :return:
        '''
        data = {'operator': operator,
                'targetId': target_id}

        url = self.format_request_url('/admin/friend/get_alias')
        return self.baby_post(url, data)

    def set_extra(self, operator, target_id, extra):
        '''
        http://domain:18080/admin/friend/set_extra

        参数	类型	必需	描述
        operator	string	是	用户ID
        targetId	string	是	对方ID
        extra	string	否	附加信息
        :return:
        '''
        data = {'operator': operator,
                'targetId': target_id,
                'extra': str(extra)}

        url = self.format_request_url('/admin/friend/set_extra')
        return self.baby_post(url, data)

    def send_request(self, user_id, friend_uid, reason, force):
        '''
        http://domain:18080/admin/friend/send_request
        参数	类型	必需	描述
        userId	string	是	用户ID
        friendUid	string	是	对方ID
        reason	string	是	附加信息
        force	bool	否	是否强制，false时会作为普通用户发出请求，可能受限与请求次数、请求间隔、拉黑等操作。true突破所有的限制

        :return:
        '''
        data = {'userId': user_id,
                'friendUid': friend_uid,
                'reason': str(reason),
                'force': str(force)}

        url = self.format_request_url('/admin/friend/send_request')
        return self.baby_post(url, data)

    def get_relation(self, first, second):
        '''
        http://domain:18080/admin/relation/get

        参数	类型	必需	描述
        first	string	是	用户ID
        second	string	是	目标用户

        :return:
        '''
        data = {'first': first,
                'second': second}

        url = self.format_request_url('/admin/relation/get')
        return self.baby_post(url, data)


if __name__ == '__main__':
    bs = BabyRelations(host='123.60.47.163',
                             http_port='80',
                             port='18080',
                             websocket_port='8083',
                             secret_key='123456',
                             token_key='',
                             debug=True)
    bs.print_info()
