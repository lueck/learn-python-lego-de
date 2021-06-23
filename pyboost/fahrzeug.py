from pylgbst.hub import MoveHub


LINKS = 1    # gegen den Uhrzeugersinn (mathematisch positive Drehung)
RECHTS = -1  # im Uhrzeigersinn (mathematisch negative Drehung)


class Einachser(MoveHub):
    """Ein einfaches einachsiges Fahrzeug auf Movehub-Basis (Vernie)."""

    # Fahrzeugparameter
    RAD_DURCHMESSER = 49.5 # mm
    UEBERSETZUNG = 1/3
    SPURWEITE = 100 # mm

    # Konstanten
    PI = 3.14

    def __init__(self, rad = RAD_DURCHMESSER, uebersetzung = UEBERSETZUNG, spurweite = SPURWEITE, *args, **kwargs):
        self.rad_durchmesser = rad
        self.uebersetzung = uebersetzung
        self.spurweite = spurweite
        super(Einachser, self).__init__(*args, **kwargs)

    def ende(self):
        """Stelle das Fahrzeug ab."""
        self.disconnect()

    @property
    def entfaltung(self):
        """Berechnet die Entfaltung bei gegebenen Fahrzeugparametern."""
        return self.PI * self.rad_durchmesser * self.uebersetzung

    def winkel_zur_strecke(self, strecke):
        """Berechnet den Winkel zu einer gewuenschten Strecke, wenn mit der
        angled-Methode gefahren werden soll."""
        return 360 * strecke / self.entfaltung

    def fahre_geradeaus(self, strecke, geschwindigkeit = .5):
        """Fahre das Fahrzeug die Strecke strecke in Milimetern."""
        self.motor_AB.angled(self.winkel_zur_strecke(strecke), geschwindigkeit, geschwindigkeit)

    def drehe(self, winkel, richtung = LINKS, geschwindigkeit = .5):
        """Drehe das Fahrzeug auf der Stelle um den Winkel winkel in der Richtung richtung herum."""
        # Bei einer 360°-Drehung muss jedes Rad einen Bogen von 180°
        # mit dem halben Radstand als Radius fahren.
        strecke = 0.5 * self.PI * self.spurweite
        geschwindigkeit_a = richtung * geschwindigkeit
        geschwindigkeit_b = richtung * geschwindigkeit * (-1)
        self.motor_AB.angled(self.winkel_zur_strecke(strecke), geschwindigkeit_a, geschwindigkeit_b)

    def fahre_bogen(self, winkel, radius, richtung = LINKS, geschwindigkeit = .2):
        """Fahre das Fahrzeug im Kreisbogen mit dem Radius radius und der
        Länge winkel. Der Radius ist der Innenradius."""
        if radius == 0:
            radius = 0.001 # Teilung durch 0 nicht definiert
        strecke_innen = 2 * self.PI * radius * winkel / 360
        strecke_außen = 2 * self.PI * (radius + self.spurweite) * winkel / 360
        strecke = (strecke_innen + strecke_außen) / 2
        geschwindigkeit_innen = geschwindigkeit
        # die Geschwindigkeit außen muss größer sein:
        geschwindigkeit_außen = (1 + (self.spurweite / radius)) * geschwindigkeit_innen
        if geschwindigkeit_außen > 1:
            geschwindigkeit_außen = 1
            geschwindigkeit_innen = (radius / (self.spurweite + radius)) # * geschwindigkeit_außen
        if richtung == LINKS:
            geschwindigkeit_a = geschwindigkeit_außen
            geschwindigkeit_b = geschwindigkeit_innen
        else:
            geschwindigkeit_a = geschwindigkeit_innen
            geschwindigkeit_b = geschwindigkeit_außen
        print("Geschwindigkeiten in der Bogenfahrt, A: %.2f, B: %.2f" % (geschwindigkeit_a, geschwindigkeit_b))
        self.motor_AB.angled(self.winkel_zur_strecke(strecke), geschwindigkeit_a, geschwindigkeit_b)


# Test
if __name__ == "__main__":
    fahrzeug = Einachser()
    fahrzeug.fahre_geradeaus(200)
    fahrzeug.drehe(180, RECHTS)
    fahrzeug.fahre_bogen(90, 100)
    fahrzeug.fahre_bogen(30, 50, RECHTS, geschwindigkeit = 1)
    fahrzeug.fahre_bogen(45, 0)
    fahrzeug.ende()
