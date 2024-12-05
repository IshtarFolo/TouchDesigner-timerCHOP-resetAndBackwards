def onValueChange(channel, sampleIndex, val, prev):
    # References aux Timers CHOPs
    timer1 = op('timer1')
    timer2 = op('timer2')
    # References aux Maths CHOPs
    math1 = op('math1')
    math2 = op('math2')
    
    # Initialise le storage si non existant pour stocker l'état du clic
    if 'clickState' not in me.storage:
        me.storage['clickState'] = 0  # Initialise a 0 (debut de cycle)
        print("ÇA DÉCOLLE : Current clickState: {clickState}")
    
    if val == 1:  # Regarde si le bouton est enfoncé
        clickState = me.storage['clickState']  # Récupère l'état actuel du clic
        print(f"Current clickState: {clickState}")

        if clickState == 0:  # Premier clic: ouvre les rideaux
            print("ON EXÉCUTE ==0 -> First click: Opening blinds. //CLOSE BLINDS")
            
            # Depart des timers
            timer1.par.play = 1
            timer1.par.start.pulse()
            timer1.par.length = 2
            
            timer2.par.play = 1
            timer2.par.start.pulse()
            timer2.par.length = 2
            
            # Configuration des Maths pour l'animation d'ouverture
            math1.par.fromrange1 = 1
            math1.par.fromrange2 = 0
            math2.par.fromrange1 = 1
            math2.par.fromrange2 = 0
            
            me.storage['clickState'] = 2  # Avance au prochain etat

        elif clickState == 1:  # Second clic: prépare l'animation de fermeture
            print("ON EXÉCUTE ==1 -> ON EST DANS 1 -> Second click: Preparing to reverse animation. ")

            me.storage['clickState'] = 2  # Avance au prochain etat

        elif clickState == 2:  # Troisième clic: ferme les rideaux et réinitialise le cycle
            print("ON EXÉCUTE ==2 -> Third click: Closing blinds. OPEN BLINDS")
            
            # On relance les timers pour les remettre à 0
            timer1.par.play = 0
            timer1.par.initialize.pulse()
            
            timer2.par.play = 0
            timer2.par.initialize.pulse()
            
            
            # Configure les Maths pour l'animation de fermeture
            math1.par.fromrange1 = 0
            math1.par.fromrange2 = 1
            math2.par.fromrange1 = 0
            math2.par.fromrange2 = 1
            
            
            # Debut des timers
            timer1.par.play = 1
            timer1.par.start.pulse()
            timer1.par.length = 2
            
            timer2.par.play = 1
            timer2.par.start.pulse()
            timer2.par.length = 2
            
            # Relancer l'etat du clic pour le prochain cycle
            me.storage['clickState'] = 0