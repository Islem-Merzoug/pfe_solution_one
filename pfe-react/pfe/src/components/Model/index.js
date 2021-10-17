import React, {useState} from 'react';
import axios from "axios";
import Loading from '../Loading';
import './Model.css';

import {
	BrowserRouter as Router,
	Switch,
	Route,
	useHistory,
	useParams
  } from "react-router-dom";
import Popup from "../Popup";
import ReCAPTCHA from "react-google-recaptcha";
import { models } from "../../services/models";

import {
	Btn, BtnInput
} from './ModelElements';
import Products from '../Products';

function Model(){
	const [buttonPopup, setButtonPopup] = useState(false)
	const [buttonPopuptwo, setButtonPopuptwo] = useState(false)
	const [selectedFile, setSelectedFile] = useState();
	const [isFilePicked, setIsFilePicked] = useState(false);
	const [isExecuted, setIsExecuted] = useState(false);
	const [faceGenderDetectType, setFaceGenderDetectType] = useState();

	const history = useHistory();
	let { id } = useParams();
	// console.log(id);
	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsFilePicked(true);		
	};

	const handleConversion = (id) => {
		setIsExecuted(true)
		const formData = new FormData();
		const selectedFileName = selectedFile.name.split('.').slice(0, -1).join('.');
		const selectedFileExtention = selectedFile.name.split('.').pop();

		console.log({
			method  : 'post',
			url : models[id].executeLink,
			data : formData,
		});

		formData.append('file', selectedFile);
		formData.append('userID', localStorage.getItem("userID"));
		formData.append('choice', faceGenderDetectType);
		
		axios({
			method  : 'post',
			url : models[id].executeLink,
			data : formData
		})
		.then((res)=>{
			console.log(res);
			console.log('res');
			setIsExecuted(false)
			history.push("/stepOne/" + id + "/" + selectedFileName + "/" + selectedFileExtention);

		})
		.catch((err) => {
			setIsExecuted(false)
			console.log("err");
			alert(err)
			throw err
			
		});
	}
	
	function onChangeRecapsha(value) {
		console.log("Captcha value:", value);
		setButtonPopup(false)
		setButtonPopuptwo(true)
	}

	function onChangeDetectTypeValue(event) {
		console.log("Detect Type Value:",event.target.value);
		setFaceGenderDetectType(event.target.value)
	}	  


	function ModelPost() {
		let { id } = useParams();

		return (

			<div style={{ margin : '3rem 3rem'}} >
				<div>
					<h1 style={{ display: 'flex', justifyContent: 'center', }} >{models[id].name}</h1>

					<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }} >
						{models[id].description}
					</div>
					<br/>

					<h4 style={{ display: 'flex', justifyContent: 'center', }} >File Extentions</h4>
					<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }} >
						{models[id].fileExtentions}
					</div>
				</div>

				<div>
					<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }} >

						<div className="column" style={{ margin: '1.5rem' }} >
							<h3 style={{ display: 'flex', justifyContent: 'left' }} >Input exemple:</h3>

							<img style={{ borderStyle: 'solid', borderColor: 'black' }} src={models[id].inputImageExempleLink} alt='Input exemple' width={"100%"}/>
						</div>

						<div className="column" style={{ margin: '1.5rem' }} >
							<h3 style={{ display: 'flex', justifyContent: 'left' }} >Output exemple:</h3>

							<img style={{ borderStyle: 'solid', borderColor: 'black' }} src={models[id].outputImageExempleLink} alt='Output exemple' width={'100%'}/>
						</div>
					</div>
				</div>


				<Popup trigger={ buttonPopup } setTrigger={ setButtonPopup }>
					<ReCAPTCHA
						sitekey="6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
						onChange={onChangeRecapsha}
					/>
				</Popup> 

				<Popup trigger={ buttonPopuptwo } setTrigger={ setButtonPopuptwo }>

					<div>
						<BtnInput type="file" name="file" onChange={changeHandler} />
						{isFilePicked ? (
							<div>
								<div>
									<p>Filename: {selectedFile.name}</p>
									<p>Filetype: {selectedFile.type}</p>
									<p>Size in bytes: {selectedFile.size} Bytes</p> 
									{/* <p>
										lastModifiedDate:{' '}
										{selectedFile.lastModifiedDate.toLocaleDateString()}
									</p> */}
									<br/>
									{isExecuted ? (
										<Loading/>
									) : (
										<p>Click here to start the process</p>
									)}

								</div>

								<div>
									<Btn onClick={() => {
										handleConversion(id)

									} 
										}>Process
									</Btn>
								</div>
							</div>


						) : (
							<p>Select a file to show details</p>
						)}

						{id == 2 ? (
							<div onChange={onChangeDetectTypeValue} >
								<input type="radio" value="detect_face" name="detection" checked /> Face
								<input type="radio" value="detect_gender" name="detection" /> Gender
							</div>

						) : (
							<p> </p>
						)}

					</div>

				</Popup> 

				<Btn disabled={ buttonPopup || buttonPopuptwo } name="file" type="button" onClick={() => setButtonPopup(true) } > Try your own image</Btn>
			
				<div style={{ padding: '3rem 0' }} >		
					<Products currentProductId = { id } />
				</div>
			</div>
		)
	}



	return(
		<Router>
			<Switch>
				<Route path="/modelDetails/:id">
					<ModelPost />
				</Route>
			</Switch>
		</Router>

	)
}

export default Model;