
let cp = require( 'child_process' );
let exec = cp.execSync;
let path = require( 'path' );
let fs = require( 'fs' );

let which = process.platform === 'win32' ? 'where' : 'which';

let output = null;
try
{
  // output = exec( 'h5cc -showconfig', { stdio : 'pipe' } );
  output = exec( `${which} h5dump`, { stdio : 'pipe' } );
}
catch( err )
{
  throw Error( `Failed to find hdf5 library installation. Reason:\n` + err.message );
}

output = output.toString();

let installation = fs.realpathSync( output.trim() );
installation = path.resolve( installation, '../..' )

if( process.argv[ 2 ] === 'settings' )
{
  console.log( getSettings( installation ) );
}
else if( process.argv[ 2 ] === 'version' )
{
  let settings = getSettings( installation )
  let version = /HDF5 Version:(.*)/.exec( settings )
  console.log( version[ 0 ] );
}
else if( process.argv[ 2 ] === 'diagnostics' )
{
  console.log( `HDF5 Installation path: ${installation}` );
  console.log( `\n${getSettings( installation )}` );
}
else
{
  console.log( installation );
}

//

function getSettings( installation )
{
  let paths =
  [
    path.join( installation, 'lib/libhdf5.settings' ),
    path.join( installation, 'share/hdf5/libhdf5.settings' ),
  ]

  for( let i = 0; i < paths.length; i++ )
  {
    if( fs.existsSync( paths[ i ] ) )
    return fs.readFileSync( paths[ i ] ).toString();
  }

  let h5cc = path.join( installation, 'bin/h5cc' );
  let execPath = `${h5cc} -showconfig`;
  console.log( `> ${execPath}` )
  let output = exec( execPath, { stdio : 'pipe' } );
  return output.toString();
}





