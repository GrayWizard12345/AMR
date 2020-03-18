from .VBPR import *
class ModelFactory:

    @staticmethod
    def newModel(args, num_users, num_items, num_image_feature=None):
        if args.model == 'VBPR' or args.model == 'AMR':
            return VBPR(args, num_users, num_items, num_image_feature)
        return None
