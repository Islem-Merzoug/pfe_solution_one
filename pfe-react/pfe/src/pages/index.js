import React from 'react';
import Products from '../components/Products';
import { models } from '../services/models'; 

const Home = () => {
  console.log(models[0] )
  return (
    <div style={{ margin: '2%' }}  >
       <h1 style={{ display: 'flex', justifyContent: 'center', margin: '2em', fontSize:"1.5rem" }} >
       Endless possibilities with computer vision, natural language processing and automated machine learning.
       </h1>
       <p style={{ display: 'flex', justifyContent: 'center', margin: '2rem' }} >
       Gather valuable business insights from images, video, and text using computer vision and natural language processing in one integrated AI Computer Vision platform.
       </p>


      <Products />

      {/* <div>
        <h1 style={{ display: 'flex', justifyContent: 'center', margin: '30px' }} >Why choose us</h1>

        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '10vh'}} >
          <div class="column" style={{ margin: '15px' }}  >
              Awesome Design
              <div style={{ color: 'gray' }}  > marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft </div>
          </div>
          <div class="column" style={{ margin: '15px' }} >
              Notification Update
              <div style={{ color: 'gray' }}  > marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft </div>
          </div>
        </div>
        
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '10vh'}} >

          <div class="column" style={{ margin: '15px' }}  >
              Quality AI Models
              <div style={{ color: 'gray' }}  > marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft </div>
          </div>
          <div class="column" style={{ margin: '15px' }} >
              Free Bug support
              <div style={{ color: 'gray' }}  > marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft </div>
          </div>
          
        </div>
      </div>

      <div>
        <h1 style={{ display: 'flex', justifyContent: 'center', marginTop: '30px' }} >Awesome feachures</h1>

        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '7vh'}} >
        marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft 
        </div>
      </div> */}


    </div>
  );
};

export default Home;
