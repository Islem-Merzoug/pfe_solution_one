import React from 'react'
import Card from '../Card/index';
import { models } from '../../services/models'; 

// import './ProductsElements'


const Products = () => {
  console.log(models[0] )
  return (
    <div>

      <div class="row">
        <div class="column">
            <Card
                id= { models[0][('id')] }
                name= { models[0][('name')] }
                image= { models[0][('image')] }
                description= { models[0][('description')] }
                detailLink= { models[0][('detailLink')] }
                inputImageExempleLink= { models[0][('inputImageExempleLink')] }
                outputImageExempleLink= { models[0][('outputImageExempleLink')] }
            />
        </div>

        <div class="column">
            <Card
                id= { models[1][('id')] }
                name= { models[1][('name')] }
                image= { models[1][('image')] }
                description= { models[1][('description')] }
                detailLink= { models[1][('detailLink')] }
                inputImageExempleLink= { models[1][('inputImageExempleLink')] }
                outputImageExempleLink= { models[1][('outputImageExempleLink')] }
            />
        </div>

        <div class="column">
            <Card
                id= { models[2][('id')] }
                name= { models[2][('name')] }
                image= { models[2][('image')] }
                description= { models[2][('description')] }
                detailLink= { models[2][('detailLink')] }
                inputImageExempleLink= { models[2][('inputImageExempleLink')] }
                outputImageExempleLink= { models[2][('outputImageExempleLink')] }
            />
        </div>
      </div>


            
        </div>
    )
}

export default Products
