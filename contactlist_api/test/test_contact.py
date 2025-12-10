# from contactlist_api.app_main.contact_api import Uday
#
# class TestContactAPI:
#
#     cls = Uday()
#
#     my_data = {
#         "firstName": "Nirmal",
#         "lastName": "Kumar",
#         "birthdate": "1970-01-01",
#         "email": "jdoe@fake.com",
#         "phone": "8005555555",
#         "street1": "1 Main St.",
#         "street2": "Apartment A",
#         "city": "Anytown",
#         "stateProvince": "KS",
#         "postalCode": "12345",
#         "country": "USA"
#     }
#
#     put_data = {
#         "firstName": "Susmita",
#         "lastName": "uday",
#         "birthdate": "1970-01-01",
#         "email": "jdoe@fake.com",
#         "phone": "8005555555",
#         "street1": "1 Main St.",
#         "street2": "Apartment A",
#         "city": "Anytown",
#         "stateProvince": "KS",
#         "postalCode": "12345",
#         "country": "USA"
#     }
#
#     patch_data = {
#         "firstName": "hima",
#         "lastName": "sree"
#     }
#
#     def test_create_contact(self):
#         resp = self.cls.create_contact(self.my_data)
#         assert resp.status_code == 201, "Contact creation failed"
#         assert resp.json()["firstName"] == "Nirmal"
#         assert "id" in resp.json()
#
#     def test_update_contact_put(self):
#         resp = self.cls.update_contact_put(self.put_data)
#         assert resp.status_code == 200, "PUT update failed"
#         assert resp.json()["firstName"] == "Susmita"
#
#     def test_update_contact_patch(self):
#         resp = self.cls.update_contact_patch(self.patch_data)
#         assert resp.status_code == 200, "PATCH update failed"
#         assert resp.json()["firstName"] == "hima"
#
#     def test_get_all_contacts(self):
#         resp = self.cls.get_all_contacts()
#         assert resp.status_code == 200
#         print(resp.json())
#
#     def test_delete_contact(self):
#         resp = self.cls.delete_contact()
#         try:
#             print(resp.json())
#         except:
#             print("Deleted", resp)