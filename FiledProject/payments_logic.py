from cardvalidator import luhn
from datetime import datetime

class Payment:
    """
    Payment Class
    """
    @staticmethod
    def process_payment(data):
        """
        Process Payment Method Logic for Processing with Validations
        """
        try:
            if not data.get('card_no') or len(data.get('card_no')) == 0:
                response = {
                    'code': 400,
                    'message': 'Card No is Mandatory'
                }
                return response
            else:
                card_valid = luhn.is_valid(data.get('card_no'))
                if not card_valid:
                    response = {
                        'code': 400,
                        'message': 'Enter Valid Card Number'
                    }
                    return response
                else:
                    card_no = data.get('card_no')

            if not data.get('card_holder') or len(data.get('card_holder')) == 0:
                response = {
                    'code': 400,
                    'message': 'Card Holder is Mandatory'
                }
                return response
            else:
                if data.get('card_holder').isalpha():
                    card_holder = data.get('card_holder')
                else:
                    response = {
                        'code': 400,
                        'message': 'Card Holder Should Alphabets Only'
                    }
                    return response

            if not data.get('expiry_date') or len(data.get('expiry_date')) == 0:
                response = {
                    'code': 400,
                    'message': 'Expiry Date is Mandatory'
                }
                return response
            else:
                exp_date = data.get('expiry_date')
                try:
                    expiry_date = datetime.strptime(exp_date,'%m/%y')
                    today_date = datetime.today()
                    t_date = datetime(today_date.year,today_date.month,1)
                except:
                    response = {
                        'code': 400,
                        'message': 'Expiry Should be MM/YY format'
                    }
                    return response
                if expiry_date < t_date:
                    response = {
                        'code': 400,
                        'message': 'Expiry Date Cannot be Past Date'
                    }
                    return response
                else:
                    expiry_date = data.get('expiry_date')

            if data.get('security_code'):
                if len(data.get('security_code')) == 3:
                    if data.get('security_code').isdigit():
                        security_code = data.get('security_code')
                    else:
                        response = {
                            'code': 400,
                            'message': 'Security Code Should be Digits'
                        }
                        return response
                else:
                    response = {
                        'code': 400,
                        'message': 'Security Code Should be 3 Digits Only'
                    }
                    return response

            if not data.get('amount'):
                response = {
                    'code': 400,
                    'message': 'Amount is Mandatory'
                }
                return response
            else:
                if isinstance(data.get('amount'), float):
                    if data.get('amount') < 0:
                        response = {
                            'code': 400,
                            'message': 'Amount Should be Positive Decimal Value'
                        }
                        return response
                    else:
                        amount = data.get('amount')
                else:
                    response = {
                        'code': 400,
                        'message': 'Amount Should Be Positive Decimal Value'
                    }
                    return response                    
            if card_no and card_holder and expiry_date and amount:
                response = {
                    'code': 200
                }
                if amount < 20:
                    response.update({
                        'message':"Payment Processed Successfully with Cheap Payment Gateway"
                    })
                elif amount > 21 and amount < 500:
                    response.update({
                        'message':"Payment Processed Successfully with Expensive Payment Gateway"
                    })
                elif amount > 500:
                    response.update({
                        'message':"Payment Processed Successfully with Premium Payment Gateway"
                    })    
                return response
        except:
            response = {
                'code': 500,
                'message':"Some External Error Occured"
            }
            return response