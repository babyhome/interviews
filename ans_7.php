<?php

function split_string( $str ) {

	$len 	= strlen( $str ); 	// 8
	$count 	= 0;
	$tx 	= "";
	echo "str: " . $str . "\n"; 	// abdcsdfd
	for( $i = 0; $i < $len; $i++ ) { 	// 7 [d]
		if( strpos( $tx, $str[$i] ) === false ) { 	// tx: df
			$tx .= (string)$str[$i]; 	// tx: df
		} else {
			echo $tx . " ";
			$count 	+= 1; 				// 2
			$tx 	= "" . $str[$i]; 	// d
			if( $i == $len - 1 ) {
				$count += 1;
			}
		}
	}

	return $count;
}


echo split_string( "adddud" );
echo split_string( "abdcsdfd" );
echo PHP_EOL;
// echo split_string( "abacadd" );

// $a = "how are you?";
// if( strpos( $a, 'hh' ) !== false ) {
// 	echo "true";
// } else {
// 	echo "false";
// }



