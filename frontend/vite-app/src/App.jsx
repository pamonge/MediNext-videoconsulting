import { useState } from 'react'
import { Routes, Route } from 'react-router-dom';
import './App.css'
import { HomeComponent } from './components/home/HomeComponent';
import { VideoCallComponent } from './components/videoCall/VideoCallComponent';
import { NotFoundComponent } from './components/notFound/NotFoundComponent';


function App() {
  return (
    <Routes>
      <Route path='/' element={ <HomeComponent /> } />
      <Route path='/video' element={ <VideoCallComponent /> } />
      <Route path='/*' element={ <NotFoundComponent /> } />
    </Routes>
  );
}

export default App
