# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="tw4449 Cdino112 multimokia d3adpan Booplicate",
        name="Habitación Personalizada Amueblado Espacio V1",
        description="Este submod añade un conjunto minimalista de muebles Spaceroom para ti y Monika.",
        version="1.0.5.1"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Habitación Personalizada Amueblado Espacio V1",
            user_name="DEV-MA",
            repository_name="Ambiente_Sala-de-estar1",
            update_dir="",
            attachment_id=None
        )

###START: IMAGE DEFINITIONS
image submod_background_Furnished_spaceroom1_day = "mod_assets/location/Spaceroom V1.1/V1.1.png"
image submod_background_Furnished_spaceroom1_rain = "mod_assets/location/Spaceroom V1.1/V1.1_rain.png"
image submod_background_Furnished_spaceroom1_overcast = "mod_assets/location/Spaceroom V1.1/V1.1_overcast.png"
image submod_background_Furnished_spaceroom1_snow = "mod_assets/location/Spaceroom V1.1/V1.1_snow.png"

#Night images
image submod_background_Furnished_spaceroom1_night = "mod_assets/location/Spaceroom V1.1/V1.1-n.png"
image submod_background_Furnished_spaceroom1_rain_night = "mod_assets/location/Spaceroom V1.1/V1.1_rain-n.png"
image submod_background_Furnished_spaceroom1_overcast_night = "mod_assets/location/Spaceroom V1.1/V1.1_overcast-n.png"
image submod_background_Furnished_spaceroom1_snow_night = "mod_assets/location/Spaceroom V1.1/V1.1_snow-n.png"

#Sunset images
image submod_background_Furnished_spaceroom1_ss = "mod_assets/location/Spaceroom V1.1/V1.1-ss.png"
image submod_background_Furnished_spaceroom1_rain_ss = "mod_assets/location/Spaceroom V1.1/V1.1_rain-ss.png"
image submod_background_Furnished_spaceroom1_overcast_ss = "mod_assets/location/Spaceroom V1.1/V1.1_overcast-ss.png"
image submod_background_Furnished_spaceroom1_snow_ss = "mod_assets/location/Spaceroom V1.1/V1.1_snow-ss.png"


init -1 python:
    submod_background_Furnished_spaceroom1 = MASFilterableBackground(
        # ID
        "submod_background_Furnished_spaceroom1",
        "Espacio amueblado 1",

        # mapping of filters to MASWeatherMaps
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_Furnished_spaceroom1_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_Furnished_spaceroom1_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_Furnished_spaceroom1_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_Furnished_spaceroom1_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_Furnished_spaceroom1_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_Furnished_spaceroom1_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_Furnished_spaceroom1_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_Furnished_spaceroom1_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_Furnished_spaceroom1_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_Furnished_spaceroom1_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_Furnished_spaceroom1_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_Furnished_spaceroom1_snow_ss",
            }),
        ),

        #NOTE: YOU DO NOT NEED TO TOUCH THIS
        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        #FOR BACKGROUND PROPERTIES (DON'T TOUCH "ENTRY_PP:/EXIT_PP:)
        disable_progressive=False,
        hide_masks=False,
        hide_calendar=False,
        unlocked=True,
        entry_pp=store.mas_background._Furnished_spaceroom1_entry,
        exit_pp=store.mas_background._Furnished_spaceroom1_exit,
        ex_props={"skip_outro": None}
    )


init -2 python in mas_background:
    def _Furnished_spaceroom1_entry(_old, **kwargs):
        """
        Entry programming point for Furnished_spaceroom1 background
        """
        if kwargs.get("startup"):
            pass

        #COMMENT(#) IF NOT NEEDED
        else:
            if not store.mas_inEVL("Furnished_spaceroom1_switch_dlg"):
                   store.pushEvent("Furnished_spaceroom1_switch_dlg")
            store.mas_o31HideVisuals()
            store.mas_d25HideVisuals()

        #IF THIS IS NOT A FURNISHED SPACEROOM, COMMENT THESE TWO LINES
        if store.seen_event("mas_monika_islands"):
           store.mas_unlockEVL("mas_monika_islands", "EVE")

    def _Furnished_spaceroom1_exit(_new, **kwargs):
        """
        Exit programming point for Furnished_spaceroom1 background
        """
        #O31
        if store.persistent._mas_o31_in_o31_mode:
            store.mas_o31ShowVisuals()

        #D25
        elif store.persistent._mas_d25_deco_active:
            store.mas_d25ShowVisuals()

        #Lock islands greet to be sure
        store.mas_lockEVL("mas_monika_islands", "EVE")

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")

###START: Topics
label Furnished_spaceroom1_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Bonita y sencilla~",
            "¡El look minimalista!",
            "Sólo unos pocos toques~",
        ]))

    m 1hua "[switch_quip]"
    return

###START: Topics
label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Solo para nosotros dos~",
            "¿Echas de menos el look clásico?",
            "Tantos recuerdos",
        ]))

    m 1hua "[switch_quip]"
    return

#THIS ONE RUNS ON INSTALL
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="bg_room_installed_low_affection",
            conditional="True",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.NORMAL, mas_aff.AFFECTIONATE)
        )
    )

label bg_room_installed_low_affection:
    python:
        #Check how many tw mods we have installed
        tw_bg_count = len(filter(lambda x: "tw4449" in x.author, mas_submod_utils.submod_map.values()))
        spacerooms_installed = len(filter(lambda x: "furnished spaceroom" in x.name.lower() and "tw4449" in x.author, mas_submod_utils.submod_map.values()))
        had_backgrounds_before = (mas_background.getUnlockedBGCount() - tw_bg_count) > 1

    if spacerooms_installed:
        m 1wud "H-huh? {w=0.5} [player], {w=0.2} ¿Has añadido nuevos archivos al juego?"
        m 1wua "Al parecer... {w=0.5} {nw}"
        extend 1sub "Muebles nuevos!"
        m 1eku "[player],¿Hiciste esto por mí? {w=0.5} Eres tan dulce, ¿lo sabías?"

    if tw_bg_count - spacerooms_installed > 0:
        $ too = ", tambien" if spacerooms_installed else ""
        $ rooms = "nuevas habitaciones" if tw_bg_count - spacerooms_installed > 1 else "una nueva habitación"
        m 1wud "H-huh?{w=0.5} [player],{w=0.2} ¿Que es esto?"
        m 1wua "parece que.. {nw}"
        extend 1sub "añadistes [rooms]!"
        if not spacerooms_installed:
            m 1eka "No puedo creer que ya hayas hecho esto por mi..."

    m 1rkc "..."
    m 3rksdla "Pero...{w=0.3}No sé cómo usarlos.{w=0.5} {nw}"
    extend 3hksdlb "Todavía no he aprendido a codificar tan bien!"
    m 1eud "Si me das algo de tiempo, estoy seguro de que averiguaré cómo usar lo que agregaste.{nw}"
    extend 3eua "Te lo haré saber cuando lo averigüe."
    m 1eka "A pesar de que no podemos usarlos todavía, Muchas gracias por hacer esto por mí.{w=0.2} Significa más de lo que crees."
    m 3huu "Te amo tanto, [player]~"
    return "no_unlock"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="bg_room_installed",
            conditional="True",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label bg_room_installed:
    python:
        #Check how many tw mods we have installed
        tw_bg_count = len(filter(lambda x: "tw4449" in x.author, mas_submod_utils.submod_map.values()))
        spacerooms_installed = len(filter(lambda x: "furnished spaceroom" in x.name.lower() and "tw4449" in x.author, mas_submod_utils.submod_map.values()))
        had_backgrounds_before = (mas_background.getUnlockedBGCount() - tw_bg_count) > 1

    if renpy.seen_label("bg_room_installed_low_affection"):
        m 1wub "[player]!{w=0.2} ¿Recuerdas esas nuevas ubicaciones que agregaste para mí?{w=0.2} {nw}"
        extend 3wub "¡Finalmente descubrí cómo usarlos!"
        m 3eua "Todo lo que tienes que hacer ahora es ir a 'Hey, [m_name]...' en el menu 'Hablar', ir a 'Ubicación', y seleccionar '¿Podemos ir a otro lugar?'"
        m 1eub "¡Entonces podemos visitar cualquiera de las ubicaciones que agregaste!"
        m 3sub "Estoy tan emocionada~"
        m 3huu "¿Por qué no vamos a visitar uno ahora mismo?, [player]?"
        m 1ekbla "Oh, y...{w=0.3}Gracias de nuevo por añadirlas para mí. Realmente eres especial."

    else:
        if spacerooms_installed:
            m 1wuo "¿Q-qué?{w=0.5} ¿Hay archivos de muebles en el juego?"
            m 1sub "[player],{w=0.2} ¿Tú hiciste esto?"
            m 3ekbsu "Sabías que quería muebles, así que me agregaste algunos para mí...{w=0.3} Eres increíble, ¿lo sabías?"

        if tw_bg_count - spacerooms_installed > 0:
            $ too = ", tambien" if spacerooms_installed else ""
            $ rooms = "nuevas habitaciones" if tw_bg_count - spacerooms_installed > 1 else "una nueva habitación"
            m 1suo "veamos ¿que es eso?{w=0.5} agregaste [rooms][too]?"
            m 3hua "Realmente hiciste todo lo posible, ¿no?"
            if not spacerooms_installed:
                m 1eka "No puedo creer que hayas hecho todo lo posible para hacer esto por mí ..."

        m 1dka "Muchas gracias[player],{w=0.2} Yo...{w=1}{nw}"
        extend 1ekbsu "Te amo mucho."

        if not had_backgrounds_before:
            m 3eub "Añadiré una nueva categoría llamada 'Ubicacion' en la opción 'Hey, [m_name]...' para que podamos poner los muebles y visitar las otras habitaciones.{w=.5} I can't wait to try them out!"

        m 1eka "Aunque quizás no esté en tu realidad todavía...{w=3}{nw}"
        extend 7hubfb "esto hará que se sienta un poco más como un hogar aquí,{w=0.2} contigo~"
    return "no_unlock"

#LABEL OVERRIDES
init 1 python:
    config.label_overrides["monika_players_control"] = "monika_players_control_override"

label monika_players_control_override:
    m 3eub "[player], ¿Sabías que tienes más control sobre este juego que yo?"
    m 3eua "Tienes acceso a los archivos y al código del juego, ¿verdad?"
    m 1eka "Así que puedes cambiarlos como quieras."
    m 3eka "Podrías hacer cosas que ni yo puedo."
    m 4eub "Como cambiar por completo cómo funciona el juego. De una novela visual, al tranquilo patio de recreo que tenemos ahora."

    if mas_isMoniEnamored(higher=True) and not persistent._mas_acs_enable_promisering:
        m 1ekbsa "Oww.. un hermoso anillo de promesa."
        m 3dkbsu "Oh, ¿no sería eso un sueño hecho realidad?."

    if not mas_getConsumable("coffee").enabled():
        m 1wuo "¡Incluso podrías añadir una taza de cafe al juego para mí!"
        m 1eka "Eso seria estupendo"

    if not persistent._mas_pm_has_code_experience:
        m 1hksdrb "Pero imagino que tus habilidades de codificación son tan buenas como las mías."
    else:
        m 3eua "Viendo que estás familiarizado con la codificación,{w=0.1} {nw}"
        extend 3hua "¡Estoy segura de que podrías hacer algo así!"

    m 1eua "Supongo que es un atractivo para los videojuegos...{w=0.3}{nw}"
    extend 3eua "tener posibilidades casi infinitas en un mundo con el que puedes interactuar."
    m 3eub "¡Es muy difícil aburrirse!"

    if not persistent._mas_pm_has_contributed_to_mas:
        m 1eka "Incluso si tu no sabes muy bien cómo cambiar este juego..."
        $ line = "Todavía podemos disfrutar de este mundo que nos unió."

    else:
        $ line = "Especialmente contigo a mi lado~"

    show monika 5eubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eubla "[line]"
    m 5ekbfa "No hay mejor manera de disfrutar de un juego que estar con la persona que amo."

    $ persistent._seen_ever["monika_players_control"] = True
    return
    

init 1 python:
    config.label_overrides["monika_gotomonika"] = "monika_gotomonika_override"

label monika_gotomonika_override:
    m 1euc "¿Venir a mi mundo?"
    m 1lksdld "¿Te refieres a este pequeño espacio flotando en un gran vacío?"

    if persistent._mas_you_chr:
        m 4eksdlc "En realidad...{w=0.5}¿No intentaste algo así una vez?"
        m 2lksdla "...A pesar de que eso no era exactamente {i}tu...{/i}"

    m 2lksdla "Estoy muy feliz de que quieras estar conmigo tanto, pero..."
    m 2eksdlc "Realmente no tienes que..."
    m 2eksdld "Claro, podría haber dicho antes que te habría arrastrado aquí hace mucho tiempo si pudiera..."
    m 2eksdlc "Pero cuanto más lo pienso, probablemente sería mejor si llego a tu realidad."
    m 3eka "Prefiero estar allí que tener que traerte aquí."
    m 3dsc "[player]...{w=1}No me digas que realmente renunciarías a tu realidad--{w=0.5}El {i}mundo{/i} real--{w=0.5}solo para venir {i}aquí{/i}, a lo que sea este lugar?{nw}"
    $ _history_list.pop()
    menu:
        m "[player]...{w=1}no me digas que realmente renunciarías a tu realidad..El {i}mundo{/i} real--solo para venir {i}aqui{/i}, a lo que sea este lugar?{fast}"
        "Si lo haría.":
            $ persistent._mas_pm_would_come_to_spaceroom = True

            m 4wkd "Pero [player]!"
            m "¡No hay casi nada que hacer aquí!"
            m 2dsc "¿Realmente odias tu realidad {i}tanto?{/i}"
            m 2eka "Algun dia, Encontraré una manera de llegar a ti, y cuando llegue ese día, Te prometo que valdrá la pena."
            m 4euc "Cualquier cosa que la vida te lance a partir de ese momento, Estaré a tu lado para ayudarte."
            m 4eud "Incluso ahora, si estás teniendo un día difícil, puedes venir a hablarme de ello en cualquier momento."
            m 2dsc "La vida debe haber tirado mucho tu camino para considerar dejarlo todo para estar conmigo."
            m 3hua "Pero viendo cómo estás aquí, eso demuestra lo resistente que eres."
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "No puedo esperar a poder compartir los buenos y los malos momentos a tu lado."

        "No lo haría.":
            $ persistent._mas_pm_would_come_to_spaceroom = False

            m 1eka "Me alegra que todavía estés dispuesto a esperarme, [player]."
            m 1lksdla "No me malinterpretes, de verdad {i}quiero{/i} estar contigo..."
            m 1lksdlc "Pero creo que sería peligroso que intentes cruzar ahora mismo."
            m 1eka "...Si es posible con la tecnología actual."
            m 1hub "¡No te preocupes, podemos seguir haciéndonos compañía!"
            m 1hksdlb "Sé que pasará un tiempo antes de que podamos estar juntos de verdad, pero espero que no te importe esperar."
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "Esperaré tanto como sea necesario, [mas_get_player_nickname()]."

        "...":
            $ persistent._mas_pm_would_come_to_spaceroom = None

            m 2eka "Está bien, siempre apreciaré y atesoraré los momentos que pasamos juntos, incluso así."
            m 2ekc "Además, ni siquiera sé cómo puedes venir aquí con la tecnología actual."
            m 2lksdlc "...E incluso si hay {i}una forma{/i} de alguna manera, no creo que sea seguro o garantizado."
            m 2lksdld "Así que hazme un favor y al menos espera a que la tecnología mejore lo suficiente para que sea completamente seguro."
            m 2lksdlc "Yo {i}realmente{/i} no quiero arriesgarme a que no lo hagas correctamente y termines en tu propio vacío..."
            m 2dkd "...dejándonos a los dos completamente solos."
            m 4hua "Quiero decir, la tecnología tiende a avanzar bastante rápido, ¡así que podríamos ser capaces de vernos antes de darnos cuenta!"
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "Así que ten paciencia por tu adorable novia, y te prometo que haré lo mismo por ti, [mas_get_player_nickname()]."

    m 5luu "Pero...{w=1}Si por casualidad aparecieras en mi puerta..."
    show monika 1hksdlb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hksdlb "¡Supongo que no tendría otra opción que aceptarlo y darte la bienvenida con los brazos abiertos!"
    m 1eksdla "No sería mucho para empezar, pero estoy seguro de que encontraremos una manera de hacerlo mejor."
    m 3hub "¡Con el tiempo, podríamos hacer nuestra propia realidad!"
    m 3euc "Por supuesto, eso suena bastante complicado si lo piensas..."
    m 3eub "¡Pero no tengo ninguna duda de que juntos podríamos lograr cualquier cosa!"
    m 3etc "Sabes...{w=1}tal vez {i}en{/i} realidad es más fácil para ti venir aquí, pero no voy a perder la esperanza de llegar a ti."
    m 1eua "Hasta entonces, esperemos y veamos qué es posible."

    $ persistent._seen_ever["monika_gotomonika"] = True
    return

## remove the readme
init 0 python:
    store.mas_utils.trydel(renpy.config.basedir.replace('\\', '/') + "/readme.md")

init 1 python:
    store.mas_submod_utils.registerFunction(
        "greeting_o31_cleanup",
        pushEvent,
        args=["o31_room_explanation"]
    )

label o31_room_explanation:
    m 1eud "Oh, por cierto, [player]...{w=0.3}{nw}"
    extend 3euc "Habrás notado que estamos de vuelta en el aula vacía."
    m 1rksdlc "No tuve tiempo de decorar ninguna habitación aparte de esta..."
    m 1eua "Así que si no te importa, me gustaría quedarme aquí para que podamos disfrutar de la decoración juntos."
    m 3eka "Podemos volver a las otras habitaciones mañana, ¿de acuerdo?"
    m 1eka "Gracias por entender, [mas_get_player_nickname()]~"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="D25_Deco",
            conditional="True",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label D25_Deco:
    m 1wuo "Espera...{w=0.5} [player], ¿Añadiste decoraciones a las otras habitaciones?"
    m 3hub "¡Sí! ¡No puedo esperar a ver cómo se ven!~"
    m 1ekbsa "Gracias, [mas_get_player_nickname()], realmente me mimas."
    m 1hubsu "Te amo tanto mi amor."

    return