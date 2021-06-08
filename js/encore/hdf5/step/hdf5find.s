#!/usr/bin/env node
let cp = require( 'child_process' );
let exec = cp.execSync;
let path = require( 'path' );
let fs = require( 'fs' );



function installationPathGet()
{
  let which = process.platform === 'win32' ? 'where' : 'which';
  let binariesToTry = [ 'h5cc', 'h5c++', 'h5dump', 'h5ccx', 'h5ls', 'h5diff', 'h5copy', 'h5stat', 'h5debug', 'h5jam' ]

  let output = null;
  let command = null;

  for( let i = 0; i < binariesToTry.length; i++ )
  {
    try
    {
      // output = exec( 'h5cc -showconfig', { stdio : 'pipe' } );
      command = `${which} ${binariesToTry[ i ]}`;
      output = exec( command, { stdio : 'pipe' } );
      break;
    }
    catch( err )
    {
    }
  }

  debugger

  if( !output )
  return defaultPathGet();

  output = output.toString().trim();

  let installation = fs.realpathSync( output );
  installation = path.resolve( installation, '../..' )

  if( process.platform === 'linux' )
  {
    if( installation === '/usr' )
    if( fs.existsSync( '/usr/lib/x86_64-linux-gnu/hdf5/serial' ) )
    installation = '/usr/lib/x86_64-linux-gnu/hdf5/serial';
  }

  return installation;
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
  let output = exec( execPath, { stdio : 'pipe' } );
  return output.toString();
}

//

function defaultPathGet()
{
  if( process.platform === 'win32' )
  return `C:/Software/hdf5`;
  else
  return `/usr/local`;
}

//

function versionsPrint()
{
  console.log( 'Node:', exec( 'node -v' ).toString().trim() );
  console.log( 'Npm:', exec( 'npm -v' ).toString().trim() );
}

//

if( typeof module !== 'undefined' && !module.parent )
{

  let installation = installationPathGet();

  if( process.argv[ 2 ] === 'settings' )
  {
    versionsPrint();
    console.log( getSettings( installation ) );
  }
  else if( process.argv[ 2 ] === 'version' )
  {
    versionsPrint();
    let settings = getSettings( installation )
    let version = /HDF5 Version:(.*)/.exec( settings )
    console.log( version[ 0 ] );
  }
  else if( process.argv[ 2 ] === 'diagnostics' )
  {
    versionsPrint();
    console.log( `HDF5 Installation path: ${installation}` );
    console.log( `\n${getSettings( installation )}` );
  }
  else
  {
    console.log( installation );
  }
}

//

module.exports =
{
  installationPathGet
};





