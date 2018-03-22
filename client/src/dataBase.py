from itertools import chain


class dataBase(object):
    """
    [summary]

    """

    def __init__(self):
        """
        [summary]
        """
        self.snakes = {}
        self.orbs = {}

    # general operations
    def iter_all(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """

        return chain(self.iter_snakes(), self.iter_orbs())

    # snake operations
    def iter_snakes(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """

        return self.snakes.iteritems()

    def iter_snakes_ids(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """

        return self.snakes.iterkeys()

    def iter_snakes_objects(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """

        return self.snakes.itervalues()

    def add_snake(self, id_, object_):
        """[summary]
        
        Arguments:
            id_ {[type]} -- [description]
            object_ {[type]} -- [description]
        """

        self.snakes[id_] = object_

    def remove_snake(self, id_):
        """[summary]
        
        Arguments:
            id_ {[type]} -- [description]
        
        Raises:
            KeyError -- [description]
        """

        if not self.snakes.has_key(id_):
            raise KeyError('No snake object with id {} to remove.'.format(id_))

        del self.snakes[id_]

    def edit_snake(self, id_, new_object):
        """[summary]
        
        Arguments:
            id_ {[type]} -- [description]
            new_object {[type]} -- [description]
        
        Raises:
            KeyError -- [description]
        """

        if not self.snakes.has_key(id_):
            raise KeyError('No snake object with id "{}" to edit.'.format(id_))

        self.snakes[id_] = new_object

    def has_snake(self, id_):
        """[summary]
        
        Arguments:
            id_ {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        return id_ in self.iter_snakes_ids()

    # orbs operations
    def iter_orbs(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """

        return self.orbs.iteritems()

    def iter_orbs_ids(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """

        return self.orbs.iterkeys()

    def iter_orbs_objects(self):
        """[summary]
        
        Returns:
            [type] -- [description]
        """

        return self.orbs.itervalues()

    def add_orb(self, id_, object_):
        """[summary]
        
        Arguments:
            id_ {[type]} -- [description]
            object_ {[type]} -- [description]
        """

        self.orbs[id_] = object_

    def remove_orb(self, id_):
        """[summary]
        
        Arguments:
            id_ {[type]} -- [description]
        
        Raises:
            KeyError -- [description]
        """

        if not self.orbs.has_key(id_):
            raise KeyError('No orb object with id {} to remove.'.format(id_))

        del self.orbs[id_]

    def edit_orb(self, id_, new_object):
        """[summary]
        
        Arguments:
            id_ {[type]} -- [description]
            new_object {[type]} -- [description]
        
        Raises:
            KeyError -- [description]
        """

        if not self.orbs.has_key(id_):
            raise KeyError('No orb object with id "{}" to edit.'.format(id_))

        self.orbs[id_] = new_object

    def has_orb(self, id_):
        """[summary]
        
        Arguments:
            id_ {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        return id_ in self.iter_orbs_ids()
