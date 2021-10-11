import PropTypes from 'prop-types';
import { Link as RouterLink } from 'react-router-dom';
// material
import {  Box, Card, Link, Typography, Stack } from '@mui/material';
import { Popup, Rating } from 'semantic-ui-react'
import { styled } from '@mui/material/styles';
// utils
import { fCurrency } from '../../../utils/formatNumber';
//
import Label from '../../Label';
import ColorPreview from '../../ColorPreview';

// ----------------------------------------------------------------------

const ProductImgStyle = styled('img')({
  top: 0,
  width: '100%',
  height: '100%',
  objectFit: 'cover',
  position: 'absolute'
});

// ----------------------------------------------------------------------

ShopProductCard.propTypes = {
  product: PropTypes.object
};

export default function ShopProductCard({ room }) {
  const { room_id } = room;
  return (
    
    <Card>
    
      <Box sx={{ pt: '100%', position: 'relative' }}>
      <ProductImgStyle alt={room_id.name} src={room_id.imgUrl} />
      </Box>
      
      
      {/* ()=>이거안하면 루프도는동안 계속 호출 */}
      <Stack spacing={2} sx={{ p: 3 }}>
        <Link to="#" color="inherit" underline="hover" component={RouterLink} onClick={()=>console.log(room_id.name)}>
          <Typography variant="subtitle1" noWrap >
            {room_id.name}
          </Typography>
        </Link>

        <Stack direction="row" alignItems="center" justifyContent="space-between">
        <Typography variant="subtitle2">
            &nbsp;
            {room_id.location}
          </Typography>
        </Stack>

      {/* product 색깔분류 */}
        {/* <Stack direction="row" alignItems="center" justifyContent="space-between">
          <ColorPreview colors={colors} />
          <Typography variant="subtitle1">
            <Typography
              component="span"
              variant="body1"
              sx={{
                color: 'text.disabled',
                textDecoration: 'line-through'
              }}
            >
              {priceSale && fCurrency(priceSale)}
            </Typography>
            &nbsp;
            {fCurrency(price)}
          </Typography>
        </Stack> */}
      </Stack>
    </Card>
    
  );
}
