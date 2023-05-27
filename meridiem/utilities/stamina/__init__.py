"""Package with stamina utilities."""


class Stamina:
    """Class to handle stamina."""

    MAX_STAMINA = 42 * 60
    """Maximum stamina in minutes."""
    GREEN_STAMINA_RATIO = 1 / 6
    """Ratio of time needed to recover one unit of green stamina."""
    YELLOW_STAMINA_RATIO = 1 / 3
    """Ratio of time needed to recover one unit of yellow stamina."""
    YELLOW_STAMINA = 39 * 60
    """Stamina threshold to start recovering yellow stamina."""
    GREEN_STAMINA = MAX_STAMINA - YELLOW_STAMINA
    """Green stamina in minutes."""

    def __init__(self, stamina: int = 0):
        """Initialize stamina.

        Args:
            stamina (int): Current stamina in minutes.
        """
        self.stamina = stamina

    def get_rest_time(self):
        """Get the time when stamina will be full."""
        resting_time = 0
        if self.stamina < self.YELLOW_STAMINA:
            # if the stamina is below the yellow stamina threshold
            # we need to recover both green and yellow stamina
            resting_time += self.GREEN_STAMINA / self.GREEN_STAMINA_RATIO
            resting_time += (
                self.YELLOW_STAMINA - self.stamina
            ) / self.YELLOW_STAMINA_RATIO
        else:
            # if the stamina is above the yellow stamina threshold
            # we only need to recover green stamina
            resting_time += (self.MAX_STAMINA - self.stamina) / self.GREEN_STAMINA_RATIO
        return resting_time
