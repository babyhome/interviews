<?php

function check_string( $input ) {

	if( !empty( $input ) && is_string( $input ) ) {
		// return preg_match( '/^[A-Z]+$/', $input );

		// check invalid
		if( ! preg_match( '/[^a-z]+/i', $input ) ) {
			if( ! preg_match( "/^[A-Z]+$/", $input ) ) {
				if( ! preg_match( "/^[a-z]+$/", $input ) ) {
					return "Mix";
				} else {
					return "All Small Letter";
				}
			} else {
				return "All Capital Letter";
			}

		} else {
			return "Invalid Input";
		}

		// // check uppercase
		// $upper 		= preg_match( "/^[A-Z]+$/", $input );

		// // check lowercase
		// $lower 		= preg_match( "/^[a-z]+$/", $input );

		// // check Mix
		// $mix 		= preg_match( '/^[A-Za-z]+/i', $input );

		// // check invalid
		// $invalid 	= preg_match( '/[^a-z]+/i', $input );

	}

	return "ok";
}


// echo check_string( "aBCEeseG" );
// echo PHP_EOL;
// echo check_string( "AXBWDGSGECSFDS" );
// echo PHP_EOL;
// echo check_string( "AXsBWD/G" );
// echo PHP_EOL;
// echo check_string( "badfsdfsdf" );
// echo PHP_EOL;
