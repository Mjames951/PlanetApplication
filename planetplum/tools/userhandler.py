def ConfirmUser(user, orgType=None, organization=None):
    if user.is_admin(): 
        return True
    match orgType:
        case "band":
            if user in organization.members.all(): return True
            if user in organization.associates.all(): return True
            if organization.label: 
                if user in organization.label.associates.all(): return True
            if user.email == organization.email: return True
        case "label":
            if user in organization.associates.all(): 
                return True
            if user.email == organization.email: 
                return True
    return False