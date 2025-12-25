from abc import ABC, abstractmethod

# =========================
# 1. Request object
# =========================
class LeaveRequest:
    def __init__(self, employee_name: str, days: int):
        self.employee_name = employee_name
        self.days = days

    def get_employee_name(self):
        return self.employee_name

    def get_days(self):
        return self.days


# =========================
# 2. Abstract Handler
# =========================

class Approver(ABC):
    def __init__(self):
        self.next_approver = None

    def set_next_approver(self, approver):
        self.next_approver = approver

    @abstractmethod
    def approve_leave(self, request: LeaveRequest):
        pass

    def approve_next(self, request: LeaveRequest):
        if self.next_approver is not None:
            self.next_approver.approve_leave(request)


# =========================
# 3. Concrete Handlers
# =========================

class TeamLeader(Approver):
    def approve_leave(self, request: LeaveRequest):
        if request.get_days() <= 2:
            print(
                f"Team Leader đã duyệt đơn {request.get_days()} ngày cho {request.get_employee_name()}"
            )
        else:
            self.approve_next(request)


class Manager(Approver):
    def approve_leave(self, request: LeaveRequest):
        if request.get_days() <= 5:
            print(
                f"Manager đã duyệt đơn {request.get_days()} ngày cho {request.get_employee_name()}"
            )
        else:
            self.approve_next(request)


class Director(Approver):
    def approve_leave(self, request: LeaveRequest):
        print(
            f"Director đã duyệt đơn {request.get_days()} ngày cho {request.get_employee_name()}"
        )


# =========================
# 4. Client / Main
# =========================

if __name__ == "__main__":

    team_lead = TeamLeader()
    manager = Manager()
    director = Director()

    team_lead.set_next_approver(manager)
    manager.set_next_approver(director)

    team_lead.approve_leave(LeaveRequest("An", 1))      
    team_lead.approve_leave(LeaveRequest("Binh", 4))  
    team_lead.approve_leave(LeaveRequest("Cuong", 10)) 
