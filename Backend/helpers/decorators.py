

def role_required(user=None):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if self.role == user:
                print('user detected')
                return func(self, *args, **kwargs)
            return 'not done'
        return wrapper
    return decorator
