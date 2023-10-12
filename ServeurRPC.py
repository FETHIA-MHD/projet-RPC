from xmlrpc.server import SimpleXMLRPCServer
import os

class Server:
    def list_files(self, path):
        file_list = os.listdir(path)
        return file_list

    def manipulation(self, action, path, file_type, new_text=None):
        response = {'success': False}

        if action == 'creation':
            try:
                if file_type == 'file':
                    open(path, 'a').close()
                elif file_type == 'repertoire':
                    os.makedirs(path)
                response['success'] = True
            except Exception as e:
                response['success'] = False

        elif action == 'suppression':
            try:
                if file_type == 'file':
                    os.remove(path)
                elif file_type == 'repertoire':
                    os.rmdir(path)
                response['success'] = True
            except Exception as e:
                response['success'] = False

        elif action == 'modification':
            try:
                with open(path, 'r+') as file:
                    content = file.read()
                    file.seek(0)
                    file.write(new_text)
                    file.truncate()
                response['success'] = True
            except Exception as e:
                response['success'] = False

        elif action == 'rename':
            try:
                new_path = os.path.join(os.path.dirname(path), new_text)
                os.rename(path, new_path)
                response['success'] = True
            except Exception as e:
                response['success'] = False



        return response


    def add_data(self, path, data):
        response = {'success': False}

        try:
            with open(path, 'a') as file:
                file.write(data)
            response['success'] = True
        except:
            response['success'] = False

        return response

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(Server())
print("Serveur en attente de connexions...")
server.serve_forever()
