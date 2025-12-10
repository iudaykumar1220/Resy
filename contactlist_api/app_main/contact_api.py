
import requests

class Uday:

    url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTFmZDY2NDNjZDY5MTAwMTU0MzMyNWMiLCJpYXQiOjE3NjM2OTQ4NTh9.UJbS07t1Sd9g9rXeTw8boaYoya00ogy2xxsu8_XWptY"
    }

    def get_all_contacts(self):
        resp = requests.get(self.url, headers=self.headers)
        return resp

    def create_contact(self, data):
        resp = requests.post(self.url, json=data, headers=self.headers)
        return resp

    def update_contact_put(self,data):
        resp = self.get_contact_id("Nirmal")
        url=self.url +"/{}".format(resp)
        resp=requests.put(url,json=data,headers=self.headers)
        return resp

    def update_contact_patch(self,data):
        resp = self.get_contact_id("Susmita")
        url=self.url +"/{}".format(resp)
        resp=requests.patch(url,json=data,headers=self.headers)
        return resp

    def get_contact_id(self,name):
        resp=self.get_all_contacts()
        resp=resp.json()
        for i in resp:
            try:
                assert i.get("firstName")==name
                print(i["_id"])
                return i["_id"]
            except:
                print("no name is found")

        return None


    def delete_contact(self):
        i_d = self.get_contact_id("Nirmal")

        if i_d is None:
            return {"error no id found"}
        url = self.url + "/{}".format(i_d)

        resp = requests.delete(url, headers=self.headers)
        return resp