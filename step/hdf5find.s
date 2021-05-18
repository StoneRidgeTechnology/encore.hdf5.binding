
let cp = require( 'child_process' );
let exec = cp.execSync;
let path = require( 'path' );
let fs = require( 'fs' );

let which = process.platform === 'win32' ? 'where' : 'which';
let binary = process.platform === 'win32' ? 'h5dump' : 'h5cc';

let output = null;
try
{
  // output = exec( 'h5cc -showconfig', { stdio : 'pipe' } );
  output = exec( `${which} ${binary}`, { stdio : 'pipe' } );
}
catch( err )
{
  throw Error( `Failed to find hdf5 library installation. Reason:\n` + err.message );
}

output = output.toString();

let installation = fs.realpathSync( output.trim() );
installation = path.resolve( installation, '../..' )

if( process.platform === 'linux' )
{
  if( installation === '/usr' )
  if( fs.existsSync( '/usr/lib/x86_64-linux-gnu/hdf5/serial' ) )
  installation = '/usr/lib/x86_64-linux-gnu/hdf5/serial';
}

if( process.argv[ 2 ] === 'version' )
{
  let settings = fs.readFileSync( path.join( installation, 'lib/libhdf5.settings' ) );
  settings = settings.toString();
  let version = /HDF5 Version:(.*)/.exec( settings )
  console.log( version[ 0 ] );
}
else
{
  console.log( installation );
}





