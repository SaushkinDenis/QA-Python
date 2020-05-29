from Test import connector


class TestEmployee:

    Employee = {
        "name": "Employee",
        "title": "EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, "
                 "PostalCode, Phone, Fax, Email",
        "default_value": "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?"
    }
    value_employee = "{number}, 'Saushkin', 'Denis', 'IT Staff', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL".format(
        number=connector.get_count_row(Employee) + 1)

    def _add_employee(self):
        connector.add_row(self.Employee, self.value_employee)

    def _update_employee(self):
        connector.update_row(self.Employee, "FirstName", "Denis", "noDenis")

    def _delete_employee(self, del_value):
        connector.delete_row(self.Employee, "FirstName", del_value)

    def test_add_employee(self):
        a = connector.get_count_row(self.Employee)
        self._add_employee()
        assert connector.get_count_row(self.Employee) - a == 1
        self._delete_employee("Denis")

    def test_update_empoyee(self):
        self._add_employee()
        self._update_employee()
        assert "noDenis" == connector.get_param_row(self.Employee, "FirstName", "LastName", "Saushkin").fetchone()[0]
        self._delete_employee("noDenis")

    def test_delete_employee(self):
        self._add_employee()
        self._delete_employee("Denis")
        assert connector.get_param_row(self.Employee, "*", "LastName", "Saushkin").fetchone() is None
