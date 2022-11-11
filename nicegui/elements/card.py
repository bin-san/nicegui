from ..element import Element


class Card(Element):

    def __init__(self) -> None:
        """Card

        Provides a container with a dropped shadow.
        """
        super().__init__('q-card')
        self.classes('column items-start q-pa-md gap-4')


class CardSection(Element):

    def __init__(self) -> None:
        super().__init__('q-card-section')


class CardActions(Element):

    def __init__(self) -> None:
        super().__init__('q-card-actions')
