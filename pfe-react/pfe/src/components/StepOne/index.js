import React, {useState} from 'react';
import {
	BrowserRouter as Router,
	Switch,
	Route,
	useHistory,
	useParams
  } from "react-router-dom";

import {
	Btn, BtnInput, BtnDownload
} from './StepOneElements';
import { models } from "../../services/models";

function StepOne(){

	function BlogPost() {
		let { id } = useParams();
		let { fileName } = useParams();
		let { extentionName } = useParams();
		let finalExportLink = models[id].exportLink + "/" + fileName + "/" + extentionName
		return (

			<div style={{ margin : '10px 50px'}}>
					<div >
						<h1 style={{ display: 'flex', justifyContent: 'center', marginTop: '30px' }} >Skin Segmentation</h1>

						<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '7vh'}} >
						Beginning with a color image, the first stage is to transform it to a skin-likelihood image. This involves transforming every pixel from RGB representation to chroma representation and determining the likelihood value based on the equation given in the previous section. The skin-likelihood image will be a gray-scale image whose gray values represent the likelihood of the pixel belonging to skin. A sample color image and its resulting skin-likelihood image are shown in Figure 3. All skin regions (like the face, the hands and the arms) were shown brighter than the non-skin region. 
						</div>
					</div>

					<div style={{ margin : '20px' }}>

						<img 
							style={{   marginLeft: 'auto',
										marginRight: 'auto',
										display: 'block',
										borderStyle: 'solid', 
										borderColor: 'black' }}  
										
							src={finalExportLink} alt='Output' />


						<div style={{ textAlign : 'center', padding : '20px'  }} >
							<a style={{ borderStyle: 'solid', borderColor: 'black', padding : '10px' }} href={finalExportLink} download>Download</a>
						</div>
					
					</div>

					
					<video width="750" height="500" controls >
						{/* <source src="/yt1s.com - TEST VIDEO.mp4" type="video/mp4"/> */}
						<source src="/bird (2).mp4" type="video/mp4"/>
						{/* <source src="/bird (2)1.mp4" type="video/mp4"/> */}

					</video>

			</div>
		);
	  }



	return(

		<Router>
			<Switch>
				<Route path="/stepOne/:id/:fileName/:extentionName">
					<BlogPost />
				</Route>
			</Switch>
		</Router>


	)
}

export default StepOne;