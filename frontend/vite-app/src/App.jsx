import { Routes, Route } from 'react-router-dom';
import { HomeComponent } from './components/home/HomeComponent';
import { VideoCallComponent } from './components/videoCall/VideoCallComponent';
import { NotFoundComponent } from './components/notFound/NotFoundComponent';
import { LoginComponent } from './components/authentification/LoginComponent';
import { RegisterComponent } from './components/authentification/RegisterComponent';
import { ProfileComponent } from './components/profile/ProfileComponent';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={ <LoginComponent /> } />
        <Route path='/profile' element={ <ProfileComponent /> } />
        <Route path='/register' element={ <RegisterComponent /> } />
        <Route path='/home' element={ <HomeComponent /> } />
        <Route path='/video' element={ <VideoCallComponent /> } />
        <Route path='/*' element={ <NotFoundComponent /> } />
      </Routes>  
    </>
  );
}

export default App
