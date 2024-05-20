from userAdminPriv import Admin

new_admin: Admin = Admin("Paolo","rgrgsg","11/11/1987")
new_admin.privileges.privileges = ["can remove user","can add user"]
new_admin.privileges.show_privileges()