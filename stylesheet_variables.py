buttons_menu_normal = """
            QPushButton{
                    background-color: rgb(101, 101, 135);
                    border-top-right-radius : 10px;
                    border-bottom-right-radius : 10px;
                }
            QPushButton::hover
                {
                    background-color: rgb(130, 130, 173);
                    border-top-right-radius : 10px;
                    border-bottom-right-radius : 10px;
                }
                            
            """

buttons_menu_active = """
            QPushButton{
                    background-color: rgb(130, 130, 173);
                    border:5px solid rgb(130, 130, 173);
                    border-left-color: rgb(85, 170, 255);
                    border-top-right-radius : 10px;
                    border-bottom-right-radius : 10px;

                }
            QPushButton::hover
                {
                    background-color: rgb(130, 130, 173);
                    border:5px solid rgb(130, 130, 173);
                    border-left-color: rgb(85, 170, 255);
                    border-top-right-radius : 10px;
                    border-bottom-right-radius : 10px;
                }

            """

red_background = """
            QPushButton{
                    background-color: rgb(255, 0, 0);
                    border-top-right-radius : 10px;
                    border-bottom-right-radius : 10px;
                }
            QPushButton::hover
                {
                    background-color: rgb(255, 0, 0);
                    border-top-right-radius : 10px;
                    border-bottom-right-radius : 10px;
                }

            """

status_gosterge_styleSheet = """

QFrame{
    border-radius:10px;

    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
    stop:{STOP_1_1} rgba(0, 172, 255, 0), stop:{STOP_1_2} rgba(0, 156, 211, 255), 
    stop:{STOP_2_1} rgba(0, 182, 211, 120), stop:{STOP_2_2} rgba(0, 0, 255, 0), 
    stop:{STOP_3_1} rgba(0, 255, 0, 0), stop:{STOP_3_2} rgba(20, 255, 0, 255), 
    stop:{STOP_4_1} rgba(0, 255, 0, 120), stop:{STOP_4_2} rgba(0, 255, 0, 0));



    }
"""

stylesheet_green = "background-color: rgb(83, 254, 53); border-radius:5px"
stylesheet_red = "background-color: rgb(254, 83, 53); border-radius:5px;"
stylesheet_yellow = "background-color: rgb(254, 254, 53); border-radius:5px;"

stylesheet_urun_barkod_secildi= "background-color:rgb(0,255,0); border: 2px solid rgb(0,255,0); border-radius:5px"
stylesheet_urun_barkod_secilmedi= "background-color:rgb(101, 101, 135); border: none; border-radius:5px"

label_mavi_slider_text = """

<p><span style=" font-weight:600; color:#9b9bff;">{VALUE}</span> </p>

"""

label_pembe_slider_text = """

<p><span style=" font-weight:600; color:#fe007e;">{VALUE}</span> </p>

"""

robot_konveyor_dolu = """
        QPushButton{
            qproperty-icon:none;
            background-image: url(:/images/icons/dolu_konveyor.png);
            {background_color}
            background-position:center;
            border-radius : 5px;
            }
        QPushButton::hover{
            background-color: rgb(101, 101, 135);
            }
    """
robot_konveyor_dolu_90 = """
        QPushButton{
            qproperty-icon:none;
            background-image: url(:/images/icons/dolu_konveyor_90.png);
            {background_color}
            background-position:center;
            border-radius : 5px;
            }
        QPushButton::hover{
            background-color: rgb(101, 101, 135);
            }
    """

robot_konveyor_bos = """
        QPushButton{
            qproperty-icon:none;
            background-image: url(:/images/icons/bos_konveyor.png);
            {background_color}
            background-position:center;
            border-radius : 5px;
            }
        QPushButton::hover{
            background-color: rgb(101, 101, 135);
            }
    """

robot_konveyor_bos_90 = """
        QPushButton{
            qproperty-icon:none;
            background-image: url(:/images/icons/robot_konveyor_90.png);
            {background_color}
            background-position:center;
            border-radius : 5px;
            }
        QPushButton::hover{
            background-color: rgb(101, 101, 135);
            }
    """



doner_konveyor_bos = """

        QPushButton{
            qproperty-icon:none;
            background-image: url(:/images/icons/doner_konveyor_bos.png);
            {background_color}
            background-position:center;
            border-radius : 10px;
        }
        QPushButton::hover
        {
            background-color: rgb(101, 101, 135);
        }
    """
doner_konveyor_dolu = """

        QPushButton{
            qproperty-icon:none;
            background-image: url(:/images/icons/doner_konveyor_dolu.png);
            {background_color}
            background-position:center;
            border-radius : 10px;
        }
        QPushButton::hover
        {
            background-color: rgb(101, 101, 135);
        }
    """
strec_konveyor_bos = """
        QPushButton{
            qproperty-icon:none;
            background-image: url(:/images/icons/strec_konveyor_90.png);
            {background_color}
            background-position:center;
            border-radius : 10px;
        }
        QPushButton::hover
        {
            background-color: rgb(101, 101, 135);
        }
    """
strec_konveyor_dolu = """
        QPushButton{
            qproperty-icon:none;
            background-image: url(:/images/icons/strec_konveyor_90_dolu.png);
            {background_color}
            background-position:center;
            border-radius : 10px;
        }
        QPushButton::hover
        {
            background-color: rgb(101, 101, 135);
        }
    """