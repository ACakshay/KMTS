<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"
   "http://www.w3.org/TR/REC-html40/loose.dtd">
<html>
<head>
<title>Music Lens - SPARQL queries</title>
<link rel="stylesheet" href="style.css">
<meta http-equiv="Content-Type" 
   content="text/html; charset=iso-8859-1">
</head>

<body background="4.png">

<div id="menu">
<ul>
<li><a href="index.html">Home</a></li>
<li><a href="ex1.php">Sparql</a></li>
<li><a href="visualization.html">Visualization</a></li>
<li><a href="about.html">About Us </a></li>

</ul>
</div>
<h3>Select a query to run</h3>
<font size = "4">
<p>
<?php
   if ($_SERVER['REQUEST_METHOD'] != 'POST'){
      $me = $_SERVER['PHP_SELF'];
?>
   <form name="form1" method="post"
         action="<?php echo $me;?>">
            <select name="sparql">
      <option value="1">Find all the albums by Manowar</option>
      <option value="2">How many band members does Nirvana have</option>
      <option value="3">How many bands are called Nirvana</option>
      <option value="4">How many artists are called John Williams?</option>
      <option value="5">Is Liz Story a person or a group?</option>
      <option value="6">In which band did Frank Sintara play?</option>  
      <option value="7">Was Keith Richards a member of The Rolling Stones? </option>
      <option value="8">Is there a group called The Notwist? </option>
      <option value="9">List all the members of The Notwist</option>
      <option value="10">How many bands are called Queen?</option>
     <option value="11">Who are the members of The Muppets?</option>
     <option value="12">Is there a group called Michael Jackson?</option>
     <option value="13">Which bands was Robbie Williams a member of ?</option>
     <option value="14">List 5 members of One Direction band</option>
     <option value="15">List top 20 tracks of The Rolling Stones based on track duration</option>
     <option value="16">List URI of Switchfoot band</option>
     <option value="17">List female members of the band ABBA</option>
     <option value="18">List top 10 tracks of The Beatles based on duration</option>
     <option value="19">List name of bands of which Paul McCartney was a member of</option>

   </select>
   
            <input type="submit" name="Submit"
               value="Run">
         
   
   </form>
<?php
   } else {
      error_reporting(0);     
       $value=$_POST['sparql'];

         

          function getUrlDbpediaAbstract($selectvalue)
      {
       
      switch($selectvalue){

         case "1":
            $input= "Manowar";
            $query =
               "PREFIX mo: <http://purl.org/ontology/mo/>
               PREFIX foaf: <http://xmlns.com/foaf/0.1/>
               PREFIX dc: <http://purl.org/dc/elements/1.1/>

               SELECT (STR(?title) AS ?stitle) ?album
               WHERE {?band foaf:name '".$input."' ;
                  foaf:made ?album .
                  ?album a mo:SignalGroup ;
                  dc:title ?title}
               ORDER BY ?title";
               break;


            
         case "2":
            $input= "Nirvana";
            $query=
               "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                  PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                  PREFIX mo: <http://purl.org/ontology/mo/>
                  SELECT COUNT(DISTINCT ?member)
                  WHERE {
                  ?band foaf:name '".$input."' .
                  ?band rdf:type mo:MusicGroup .
                  ?member mo:member_of ?band .
               }";
               break;

         case "3":
            $input= "Nirvana";
            $query= 
               "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX foaf: <http://xmlns.com/foaf/0.1/>
               PREFIX mo: <http://purl.org/ontology/mo/>
               SELECT COUNT(DISTINCT ?artist)
               WHERE {
               ?artist rdf:type mo:MusicGroup .
               ?artist foaf:name '".$input."' .
               }";
               break;
         case "4":
            $input="John Williams";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX foaf: <http://xmlns.com/foaf/0.1/>
               PREFIX mo: <http://purl.org/ontology/mo/>
               SELECT COUNT(DISTINCT ?artist)
               WHERE {
               ?artist rdf:type mo:SoloMusicArtist .
               ?artist foaf:name '".$input."' .
               }";
               break;
         case "5":
            $input="Liz Story";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            SELECT DISTINCT ?artisttype
            WHERE {
            ?artist foaf:name '".$input."'.
            ?artist rdf:type ?artisttype .
            FILTER (?artisttype != mo:MusicArtist)
            }";
            break;
         case "6":
            $input="Frank Sinatra";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            SELECT DISTINCT ?band ?name
            WHERE {
            ?artist foaf:name '".$input."' .
            ?artist mo:member_of ?band .
            ?band foaf:name ?name .
            }";
            break;
         case "7":
            $input="Keith Richards";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            ASK
            WHERE {
            ?artist foaf:name '".$input."' .
            ?artist mo:member_of ?band .
            ?band foaf:name 'The Rolling Stones' .
            }";
            break;
         case "8":
            $input="The Notwist";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            ASK
            WHERE {
            ?artist rdf:type mo:MusicGroup .
            ?artist foaf:name '".$input."' .
            }";
            break;
         case "9":
             $input="The Notwist";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            SELECT DISTINCT ?artist ?name
            WHERE {
            ?artist mo:member_of ?band .
            ?band foaf:name '".$input."' .
            ?artist foaf:name ?name .
            }";
            break;
         case "10":
              $input="Queen";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            SELECT COUNT(DISTINCT ?artist)
            WHERE {
            ?artist rdf:type mo:MusicGroup .
            ?artist foaf:name '".$input."' .
            }";
            break;
         case "11":
              $input="The Muppets";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX mo: <http://purl.org/ontology/mo/>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            SELECT DISTINCT ?artist ?artistname
            WHERE {
            ?band foaf:name '".$input."' .
            ?artist mo:member_of ?band.
            ?artist foaf:name ?artistname .
            }";
            break;
         case "12":
              $input="Michael Jackson";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            ASK
            WHERE {
            ?artist rdf:type mo:MusicGroup .
            ?artist foaf:name '".$input."' .
            }";
            break;
         case "13":
              $input="Robbie Williams";
            $query=
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            SELECT DISTINCT ?band ?bandname
            WHERE {
            ?artist foaf:name '".$input."' .
            ?artist mo:member_of ?band .
            ?band foaf:name ?bandname .
            }";
            break;
			
		case "14": $input = "One Direction";
			$query =
			"select distinct ?name where {
			?onedirection <http://xmlns.com/foaf/0.1/name> '".$input."' .
			?member <http://purl.org/ontology/mo/member_of> ?onedirection.
			?member <http://xmlns.com/foaf/0.1/gender> 'male' .
			?member <http://xmlns.com/foaf/0.1/name> ?name .
			} LIMIT 5";
			break;
				
		case "15": $input = "The Rolling Stones";
			$query =
			"PREFIX mo: <http://purl.org/ontology/mo/>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			SELECT ?release ((SUM(xsd:double(?duration/60000))) AS ?avg)
			WHERE {
			?band foaf:name '".$input."';
			foaf:made ?release .
			?release mo:record ?record .
			?record mo:track ?track .
			?track mo:duration ?duration .}
			GROUP BY ?release
			ORDER BY DESC(?avg)
			LIMIT 20";
			break;
				
		case "16": $input = "switchfoot";
			$query =
			"PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX mo: <http://purl.org/ontology/mo/>
			SELECT ?name ?artist 
			WHERE {
			?artist a mo:MusicArtist
			. ?artist foaf:name ?name
			. FILTER(regex(str(?name), '".$input."', 'i'))}";
			break;
				
		case "17": $input = "ABBA";
			$query =
			"select distinct ?name where {
			?abba <http://xmlns.com/foaf/0.1/name> '".$input."' .
			?member <http://purl.org/ontology/mo/member_of> ?abba .
			?member <http://xmlns.com/foaf/0.1/gender> 'female' .
			?member <http://xmlns.com/foaf/0.1/name> ?name
			} LIMIT 5";
			break;
				
		case "18": $input = "The Beatles";
			$query =
			"PREFIX mo: <http://purl.org/ontology/mo/>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			SELECT ?release ((SUM(xsd:double(?duration/60000))) AS ?avg)
			WHERE {
			?band foaf:name '".$input."';
			foaf:made ?release .
			?release mo:record ?record .
			?record mo:track ?track .
			?track mo:duration ?duration .}
			GROUP BY ?release
			ORDER BY DESC(?avg)
			LIMIT 10";
			break;
				
		case "19": $input = "Paul McCartney";
			$query =
			"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX mo: <http://purl.org/ontology/mo/>
			SELECT DISTINCT ?band ?bandname
			WHERE {
			?artist foaf:name '".$input."' .
			?artist mo:member_of ?band .
			?band foaf:name ?bandname .
			}";
			break;
      }  
      $format = 'json';


      $searchUrl = 'http://linkedbrainz.org/sparql?'
      .'query='.urlencode($query)
      .'&format='.$format;
      //echo $searchUrl;
      return $searchUrl;

      }


      function printArray($array, $spaces = "")
      {
      $retValue = "";
      if(is_array($array))
      {
      $spaces = $spaces
      ."&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
      $retValue = $retValue."<br/>";
      foreach(array_keys($array) as $key)
      {
      $retValue = $retValue.$spaces
      ."<strong>".$key."</strong>"
      .printArray($array[$key],
      $spaces);
      }
      $spaces = substr($spaces, 0, -30);
      }
      else $retValue =
      $retValue." - ".$array."<br/>";
      return $retValue;
      }
      function request($url){
      // is curl installed?
      if (!function_exists('curl_init')){
      die('CURL is not installed!');
      }
      // get curl handle
      $ch= curl_init();
      // set request url
      curl_setopt($ch,
      CURLOPT_URL,
      $url);
      // return response, don't print/echo
      curl_setopt($ch,
      CURLOPT_RETURNTRANSFER,
      true);
      /*
      Here you find more options for curl:
      http://www.php.net/curl_setopt
      */ 
      $response = curl_exec($ch);
      curl_close($ch);
      return $response;
      }

      function printOutput($responseArray, $value){
         switch ($value) {
            case "1":
                  echo "<table style='width:80%' border='1'>";
                  for ($x = 0; $x <=50; $x++) {
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["stitle"]["value"];
                  echo "</td>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["album"]["value"];

                  echo "</td>";
                  echo "</tr>";


                  }
                  echo "</table>";
               break;
            case "2":
                  echo "The number of members in a band :";
                  echo $responseArray["results"]["bindings"][0]["callret-0"]["value"];
                  break;
            case "3":
                  echo "The number of bands which are called Nirvana :";
                  echo $responseArray["results"]["bindings"][0]["callret-0"]["value"];
                  break;
            case "4":
                  echo "The number of artists who are called John Williams:";
                  echo $responseArray["results"]["bindings"][0]["callret-0"]["value"];
                  break;
            case "5":
                  echo "The Liz Story is of artists type: ";
                  echo $responseArray["results"]["bindings"][0]["artisttype"]["value"];
                  break;
            case "6":
                  echo "Frank Sintara plays in following band: ";
                  echo "<table style='width:80%' border='1'>";
                  
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][0]["band"]["value"];
                  echo "</td>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][0]["name"]["value"];

                  echo "</td>";
                  echo "</tr>";


                  echo "</table>";
                  break;
            case "7":
                  echo "Was Keith Richards a member of The Rolling Stones? ";
                  $output= $responseArray["boolean"];
                  if($output==1){
                     echo " YES ";
                  }
                  else {
                     echo "NO";
                  }
                  break;
            case "8":
                  echo "Is there a group called The Notwist?";
                  $output= $responseArray["boolean"];
                  if($output==1){
                     echo " YES ";
                  }
                  else {
                     echo "NO";
                  }
                  break;
            
            case "9":
                  echo "List all the members of The Notwist";
                  echo "<table style='width:80%' border='1'>";
                  for ($x = 0; $x <=2; $x++) {
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["name"]["value"];

                  echo "</td>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["artist"]["value"];
                  
                  echo "</td>";
                  echo "</tr>";


                  }
                  echo "</table>";
               break;
            case "10":
                  echo "How many bands are called Queen?  ";

                  echo $responseArray["results"]["bindings"][0]["callret-0"]["value"];
                  break;
            case "11":
                  echo "The members of Muppets are:";
                  echo "<table style='width:80%' border='1'>";
                  for ($x = 0; $x <=8; $x++) {
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["artistname"]["value"];
                  echo "</td>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["artist"]["value"];

                  echo "</td>";
                  echo "</tr>";


                  }
                  echo "</table>";
                 // echo $responseArray["results"]["bindings"][0]["callret-0"]["value"];
                  break;
            case "12":
                  
                  echo "Is there a group called Michael Jackson? ";
                  $output= $responseArray["boolean"];
                  if($output==1){
                     echo " YES ";
                  }
                  else {
                     echo "NO";
                  }
                  break;
            case "13":
                  echo "Robbie Williams is a member of following bands: ";
                  echo "<br>";
                  echo "<table style='width:80%' border='1'>";
                  
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][0]["bandname"]["value"];
                  echo "</td>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][0]["band"]["value"];

                  echo "</td>";
                  echo "</tr>";


                  echo "</table>";
                  break;
				  
			case "14": echo "5 members of One Direction band";
					echo "<table style='width:80%' border='1'>";
                  for ($x = 0; $x < 5; $x++) {
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["name"]["value"];

                  echo "</td>";
                  echo "</tr>";
                  }
                  echo "</table>";
				break;
				
			case "15": echo "Top 20 tracks of The Rolling Stones based on track duration";
					echo "<table style='width:80%' border='1'>";
                  for ($x = 0; $x < 20; $x++) {
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["release"]["value"];
                  echo "</td>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["avg"]["value"];
                  echo "</td>";
                  echo "</tr>";
                  }
                  echo "</table>";
				break;
				
			case "16": echo "The URI of Switchfoot band is ";
				echo $responseArray["results"]["bindings"][0]["artist"]["value"];
				break;
				
			case "17": echo "Female members of the band ABBA";
				echo "<table style='width:80%' border='1'>";
                  for ($x = 0; $x < 1; $x++) {
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["name"]["value"];
                  echo "</td>";
                  echo "</tr>";
                  }
                  echo "</table>";
				break;
				
			case "18": echo "Top 10 tracks of The Beatles based on duration";
					echo "<table style='width:80%' border='1'>";
                  for ($x = 0; $x < 10; $x++) {
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["release"]["value"];
                  echo "</td>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["avg"]["value"];
                  echo "</td>";
                  echo "</tr>";
                  }
                  echo "</table>";
				break;
				
			case "19": echo "Name of bands of which Paul McCartney was a member of";
				echo "<table style='width:80%' border='1'>";
                  for ($x = 0; $x < 3; $x++) {
                  echo "<tr>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["band"]["value"];
                  echo "</td>";
                  echo "<td>";
                  echo $responseArray["results"]["bindings"][$x]["bandname"]["value"];
                  echo "</td>";
                  echo "</tr>";
                  }
                  echo "</table>";
				break;
         

         }
      }
      $requestURL = getUrlDbpediaAbstract($value);
      $responseArray = json_decode(request($requestURL),true);

	//echo printArray($responseArray);
     echo printOutput($responseArray,$value);


}

?>
</font>
</body>
</html>