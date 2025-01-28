import React from 'react';
import { Card, Button } from 'antd';
import BuyButton from './BuyButton';
const ProductCard = (props) => {
  const { product } = props

    return (
      <>
    <Card
      title="Каталог товаров"
      style={{
        width: 700,
        height: 600
      }}
      className='text-[30px]'>
        <p class='text-[30px] pt-35 pl-40'>Название: {product.name}</p>
        <p class='text-[30px] pl-40'>Цена: {product.price}</p>
        <p class='text-[30px] pl-40'>Количество: {product.count}</p>
        <div className='pt-10 pl-65'>
        <BuyButton/>
        </div>
    </Card>
      </>
    )
};

export default ProductCard;