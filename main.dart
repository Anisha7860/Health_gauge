import '../flutter_flow/flutter_flow_theme.dart';
import '../flutter_flow/flutter_flow_util.dart';
import '../flutter_flow/flutter_flow_widgets.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class HomePageWidget extends StatefulWidget {
  HomePageWidget({Key key}) : super(key: key);

  @override
  _HomePageWidgetState createState() => _HomePageWidgetState();
}

class _HomePageWidgetState extends State<HomePageWidget> {
  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      backgroundColor: Color(0xFF2C3132),
      body: SafeArea(
        child: Stack(
          children: [
            Stack(
              children: [
                Padding(
                  padding: EdgeInsets.fromLTRB(0, 0, 0, 1),
                  child: Stack(
                    children: [
                      Stack(
                        children: [
                          Padding(
                            padding: EdgeInsets.fromLTRB(23, 320, 0, 0),
                            child: FFButtonWidget(
                              onPressed: () {
                                print('Button pressed ...');
                              },
                              text: 'Mental Health',
                              options: FFButtonOptions(
                                width: 350,
                                height: 170,
                                color: Color(0xFFE30808),
                                textStyle: FlutterFlowTheme.title1.override(
                                  fontFamily: 'Work Sans',
                                  color: Colors.black,
                                  fontWeight: FontWeight.bold,
                                ),
                                borderSide: BorderSide(
                                  color: Color(0xFF222222),
                                ),
                                borderRadius: 25,
                              ),
                            ),
                          ),
                          Padding(
                            padding: EdgeInsets.fromLTRB(23, 520, 0, 0),
                            child: FFButtonWidget(
                              onPressed: () {
                                print('Button pressed ...');
                              },
                              text: 'Physical Health',
                              options: FFButtonOptions(
                                width: 350,
                                height: 170,
                                color: Color(0xFFE30808),
                                textStyle: FlutterFlowTheme.title1.override(
                                  fontFamily: 'Poppins',
                                  color: Colors.black,
                                  fontWeight: FontWeight.bold,
                                ),
                                borderSide: BorderSide(
                                  color: Colors.transparent,
                                ),
                                borderRadius: 25,
                              ),
                            ),
                          )
                        ],
                      ),
                      Padding(
                        padding: EdgeInsets.fromLTRB(15, 20, 0, 0),
                        child: Text(
                          'Health Guage',
                          style: FlutterFlowTheme.bodyText1.override(
                            fontFamily: 'Open Sans Condensed',
                            color: Color(0xFFA8A0A0),
                            fontSize: 50,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      )
                    ],
                  ),
                ),
                Padding(
                  padding: EdgeInsets.fromLTRB(15, 140, 0, 0),
                  child: Text(
                    'Always give first priority to Health because wealth will come and go  but your health wont. So always be    in shape and check out your health status',
                    textAlign: TextAlign.justify,
                    style: FlutterFlowTheme.bodyText1.override(
                      fontFamily: 'Poppins',
                      color: Color(0xFFA8A0A0),
                      fontSize: 20,
                    ),
                  ),
                )
              ],
            ),
            Padding(
              padding: EdgeInsets.fromLTRB(250, 130, 0, 0),
              child: Image.network(
                '-therapy-physician-hea',
                width: 100,
                height: 100,
                fit: BoxFit.cover,
              ),
            )
          ],
        ),
      ),
    );
  }
}
