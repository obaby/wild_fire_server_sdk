from baby_server import BabyServer

# https://docs.wildfirechat.cn/server/admin_api/user_api.html
# obaby@mars
# by:obaby
# http://www.h4ck.org.cn
# http://www.obaby.org.cn
# http://www.findu.co

class BabyUser(BabyServer):

    def get_token(self, user_id, client_id, platform):
        '''
        http://domain:18080/admin/user/get_token
        userId	string	是	用户ID
        clientId	string	是	客户端ID
        platform	int	是	平台类型iOS 1, Android 2, Windows 3, OSX 4, WEB 5, 小程序 6，linux 7
        :return:
        '''
        data = {'userId': user_id,
                'clientId': client_id,
                'platform': str(platform)}

        url = self.format_request_url('/admin/user/get_token')
        return self.baby_post(url, data)

    def create_update_user(self, user_id, name, display_name=None, portrait=None, mobile=None, email=None, address=None,
                           company=None, extra=None):
        '''
        http://domain:18080/admin/user/create
        参数	类型	必需	描述
        userId	string	否	用户ID，如果传空，系统会自动生成一个用户id。必须保证唯一性。
        name	string	是	帐号名，必须保证唯一性。
        displayName	string	是	显示名字
        portrait	string	否	用户头像
        mobile	string	否	用户手机号码
        email	string	否	用户邮箱
        address	string	否	用户地址
        company	string	否	用户公司
        extra	string	否	附加信息
        :return:
        '''
        data = {'userId': user_id,
                'name': name,
                'displayName': display_name}
        if portrait:
            data['portrait'] = portrait
        if mobile:
            data['mobile'] = mobile
        if email:
            data['email'] = email
        if address:
            data['address'] = address
        if company:
            data['company'] = company
        if extra:
            data['extra'] = extra

        url = self.format_request_url('/admin/user/create')
        return self.baby_post(url, data)

    def create_update_bot(self, user_id, name, owner, display_name=None, portrait=None, mobile=None, email=None,
                          address=None,
                          company=None, extra=None, secret=None, callback=None, robotExtra=None):
        '''
        http://domain:18080/admin/robot/create
        参数	类型	必需	描述
        userId	string	否	用户ID，如果传空，系统会自动生成一个用户id
        name	string	是	登录名
        displayName	string	是	显示名字
        portrait	string	否	用户头像
        mobile	string	否	用户手机号码
        email	string	否	用户邮箱
        address	string	否	用户地址
        company	string	否	用户公司
        extra	string	否	附加信息
        owner	string	是	机器人拥有者
        secret	string	否	机器人密钥
        callback	string	否	机器人消息回掉地址
        robotExtra	string	否	机器人附加信息
        :return:
        '''
        data = {'userId': user_id,
                'name': name,
                'displayName': display_name,
                'owner': owner}
        if portrait:
            data['portrait'] = portrait
        if mobile:
            data['mobile'] = mobile
        if email:
            data['email'] = email
        if address:
            data['address'] = address
        if company:
            data['company'] = company
        if extra:
            data['extra'] = extra
        if secret:
            data['secret'] = secret
        if callback:
            data['callback'] = callback
        if robotExtra:
            data['robotExtra'] = robotExtra

        url = self.format_request_url('/admin/robot/create')
        return self.baby_post(url, data)

    def update_user(self, user_id, display_name=None, portrait=None, mobile=None, email=None, address=None,
                    company=None, extra=None):
        '''
        http://domain:18080/admin/user/update
        参数	类型	必需	描述
        flag	int	是	更新用户信息的字段信息，
        第0bit位为1时更新userInfo中的昵称信息，
        第1位更新头像，
        第2位更新性别，
        第3更新电话，
        第4位更新email，
        第5位更新地址，
        第6位更新公司，
        第7位更新社交信息，
        第8位更新extra信息，
        第9位更新name信息。
        比如更新用户头像和昵称，flag应该位 0x03
        userInfo	json	是	要更新的用户信息，与创建用户参数一致，注意必须带有userId参数，其它带上flag指定修改的字段
        :return:
        '''
        flag = 1
        data = {'userId': user_id}
        if display_name:
            data['displayName'] = display_name
        if portrait:
            data['portrait'] = portrait
        if mobile:
            data['mobile'] = mobile
        if email:
            data['email'] = email
        if address:
            data['address'] = address
        if company:
            data['company'] = company
        if extra:
            data['extra'] = extra

        url = self.format_request_url('/admin/user/update')
        w_data = {'flag': flag,
                  'userInfo': data}
        return self.baby_post(url, w_data)

    def get_user_info(self, user_id=None, name=None, mobile=None):
        '''
        http://domain:18080/admin/user/get_info
        参数	类型	必需	描述
        userId	string	否（三个参数必须且只能存在一个）	用户ID
        name	string	否（三个参数必须且只能存在一个）	登录名
        mobile	string	否（三个参数必须且只能存在一个）	用户手机号码
        :return:
        '''
        data = {}
        if user_id:
            data = {'userId': user_id}

        if name:
            data = {'name': name}

        if mobile:
            data = {'mobile': mobile}
        if not data:
            if self.debug:
                print('[E] there must be an param')
            return None
        url = self.format_request_url('/admin/user/get_info')
        return self.baby_post(url, data)

    def update_block_status(self, user_id, status):
        '''
        http://domain:18080/admin/user/update_block_status
        参数	类型	必需	描述
        userId	string	是	用户ID
        status	int	是	用户状态，0 正常；1 被禁言，2 被封禁
        :return:
        '''
        data = {'userId': user_id,
                'status': str(status)}
        url = self.format_request_url('/admin/user/update_block_status')
        return self.baby_post(url, data)

    def check_block_status(self, user_id):
        '''
        http://domain:18080/admin/user/check_block_status

        参数	类型	必需	描述
        userId	string	是	用户ID
        :param user_id:
        :return:
        '''
        data = {'userId': user_id}
        url = self.format_request_url('/admin/user/check_block_status')
        return self.baby_post(url, data)

    def get_blocked_list(self, user_id):
        '''
        http://domain:18080/admin/user/get_blocked_list
        参数	类型	必需	描述
        userId	string	是	用户ID
        :param user_id:
        :return:
        '''
        data = {'userId': user_id}
        url = self.format_request_url('/admin/user/get_blocked_list')
        return self.baby_post(url, data)

    def onlinestatus(self, user_id):
        '''
        http://domain:18080/admin/user/onlinestatus
        参数	类型	必需	描述
        userId	string	是	用户ID
        :return:
        '''
        data = {'userId': user_id}
        url = self.format_request_url('/admin/user/onlinestatus')
        return self.baby_post(url, data)


if __name__ == '__main__':
    bs = BabyUser(host='123.60.47.163',
                  http_port='80',
                  port='18080',
                  websocket_port='8083',
                  secret_key='123456',
                  token_key='',
                  debug=True)
    bs.print_info()
    res = bs.get_token('1011', 'abc', '1')
    # print(res)
    bs.get_user_info(user_id='101')
